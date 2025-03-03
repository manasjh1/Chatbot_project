### 📚 RAG-Based Chatbot for College

This is an AI-powered chatbot designed to handle college-related queries using **Retrieval-Augmented Generation (RAG)**. The chatbot integrates **LLM (Large Language Models), vector databases (Pinecone), and a knowledge graph (Neo4j)** to provide accurate and context-aware responses to students.

## 🚀 Features
- **RAG-Powered Responses**: Combines retrieval and generative AI for better accuracy.
- **Vector Database Integration**: Uses **Pinecone** for efficient similarity search.
- **Knowledge Graph Support**: Uses **Neo4j** to enhance structured query understanding.
- **FastAPI Backend**: Lightweight and scalable API for chatbot interactions.
- **MongoDB for Chat History**: Stores previous conversations to improve user experience.
- **Cost-Effective Deployment**: Optimized for budget-friendly LLM inference using **Groq API**.

## 🛠️ Tech Stack
- **Backend**: FastAPI, Python
- **Database**: MongoDB (Chat history), Pinecone (Vector DB), Neo4j (Graph DB)
- **Machine Learning**: LLaMA 3.2 1B (Hugging Face) / LLaMA 3.3 70B (Groq API)
- **Deployment**: Google Cloud, Docker

## 📂 Project Structure
```
📦 RAG-Chatbot
├── app.py          # Main entry point for chatbot API
├── db_handler.py   # Handles MongoDB interactions
├── helper.py       # Vector database connection and neo4j connection
├── prompt.py       # Prompt engineering logic
├── requirements.txt # Dependencies
└── README.md       # Project documentation
```

## 🔧 Installation & Setup
1. **Clone the repository**
   ```sh
   git clone https://github.com/your-username/rag-chatbot.git
   cd rag-chatbot
   ```
2. **Create a virtual environment** (Optional but recommended)
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set up environment variables** (`.env` file):
   ```env
   MONGO_URI="your_mongodb_uri"
   PINECONE_API_KEY="your_pinecone_api_key"
   NEO4J_URI="your_neo4j_uri"
   GROQ_API_KEY="your_groq_api_key"
   ```
5. **Run the chatbot API**
   ```sh
   uvicorn app:app --reload
   ```

## 📌 Usage
- Send a **query** to the chatbot API endpoint.
- The bot retrieves relevant information from **Pinecone (vector DB) and Neo4j (graph DB)**.
- The refined context is passed to **LLM (Groq API)** for response generation.
- The response is returned and **stored in MongoDB** for future reference.

## 🛠️ Future Enhancements
- Improve response **latency and efficiency**.
- Expand dataset for **better query understanding**.
- Deploy as a **user-friendly web interface**.
- Add **multilingual support** for diverse student queries.

## 🤝 Contributing
Contributions are welcome! Feel free to open issues and submit pull requests.

## 📜 License
This project is licensed under the **MIT License**.

## 🌟 Acknowledgments
- **Open-source AI models** from Hugging Face.
- **Groq API** for LLM inference.
- **Pinecone & Neo4j** for efficient retrieval and knowledge graph support.

--- ![Screenshot 2025-03-03 223606](https://github.com/user-attachments/assets/65fd78e8-03a5-4bb6-a360-4942ff51b13d)

### ⭐ If you like this project, consider giving it a **star** on GitHub! ⭐

