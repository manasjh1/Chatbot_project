from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings
from src.prompt import system_prompt
from pymongo import MongoClient
from datetime import datetime
from typing import Dict, List
from pydantic import BaseModel
from langchain_pinecone import PineconeVectorStore
from pinecone.grpc import PineconeGRPC as Pinecone
from groq import Groq
from neo4j import GraphDatabase
from thefuzz import process
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

# Initialize FastAPI app
app = FastAPI(title="RAG Chatbot API with Neo4j")

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Initialize embeddings and vector store
embeddings = download_hugging_face_embeddings()
index_name = "bot"
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 5})

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

# Connect to MongoDB
mongo_client = MongoClient(MONGO_URI)
db = mongo_client[MONGO_DB_NAME]
collection = db[COLLECTION_NAME]

# Initialize Neo4j driver
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))

# Define a list of common queries to match against for fuzzy correction
common_queries = ["hostel fees", "admission process", "Gautam Buddha University", "courses offered", "faculty details"]

def correct_query(query: str) -> str:
    """Uses fuzzy matching to correct user input based on predefined queries."""
    best_match, score = process.extractOne(query, common_queries)
    return best_match if score > 80 else query  # Only correct if confidence is high

def query_neo4j(entity):
    """Searches Neo4j for information related to the entity."""
    with driver.session() as session:
        query = """
        MATCH (n) WHERE toLower(n.id) CONTAINS toLower($entity)
        RETURN n.id AS entity_id, labels(n) AS entity_type LIMIT 2
        """
        response = session.run(query, entity=entity)
        return [f"{record['entity_id']} ({record['entity_type'][0]})" for record in response]

async def handle_query(query: str) -> str:
    query = correct_query(query)  # Apply fuzzy matching correction
    retrieved_docs = retriever.invoke(query)
    
    # Combine context from vector DB
    vector_context = "\n".join(doc.page_content for doc in retrieved_docs) if retrieved_docs else ""
    
    # Query Neo4j for structured data
    neo4j_data = query_neo4j(query)
    structured_context = "\n".join(neo4j_data) if neo4j_data else ""
    
    combined_context = f"Vector DB Context:\n{vector_context}\n\nNeo4j Context:\n{structured_context}"
    
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            system_prompt,
            {"role": "user", "content": f"{combined_context}\n\nUser question: {query}"}
        ],
        temperature=0.3,
        max_completion_tokens=300,
        top_p=0.7,
        stream=False,
        stop=None,
    )
    
    return completion.choices[0].message.content.strip()

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

@app.post("/get")
async def chat(msg: str = Form(...)):
    print("User Input:", msg)
    response = await handle_query(msg)
    print("Response:", response)
    collection.insert_one({"user_message": msg, "bot_response": response, "timestamp": datetime.utcnow()})
    return JSONResponse(content={"response": response})

@app.get("/history")
async def chat_history():
    history = list(collection.find().sort("timestamp", -1).limit(10))
    for record in history:
        record["_id"] = str(record["_id"])
    return JSONResponse(content={"history": history})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)
