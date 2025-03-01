from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader, DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
import os
from py2neo import Graph
import yake

load_dotenv()

# Load environment variables
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

def load_pdf_file(data_path):
    pdf_loader = DirectoryLoader(data_path, glob="*.pdf", loader_cls=PyPDFLoader)
    txt_loader = DirectoryLoader(data_path, glob="*.txt", loader_cls=TextLoader)

    pdf_documents = pdf_loader.load()
    txt_documents = txt_loader.load()

    return pdf_documents + txt_documents  

def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks

def download_hugging_face_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')  
    return embeddings

def extract_keywords(text):
    keyword_extractor = yake.KeywordExtractor(lan="en", n=2, dedupLim=0.9, top=10)
    keywords = keyword_extractor.extract_keywords(text)
    return [kw[0] for kw in keywords]

def query_neo4j(query):
    try:
        graph = Graph(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
        keywords = extract_keywords(query)
        cypher_query = (
            "MATCH (n) WHERE " + " OR ".join([f"n.name CONTAINS '{kw}'" for kw in keywords]) + " RETURN n LIMIT 5"
        )
        result = graph.run(cypher_query).data()
        return result
    except Exception as e:
        print(f"Neo4j query error: {e}")
        return []
