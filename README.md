# 🚀 AI Help Bot for Satellite Data Access (MOSDAC)

A domain-specific, **Retrieval-Augmented Generation (RAG)** chatbot built for **ISRO’s MOSDAC Portal**, empowering users—**researchers, analysts, and citizens**—to retrieve **real-time, contextual, and geospatial satellite data** via natural language queries.

Developed for the **Bharatiya Antariksh Hackathon 2025**
**Team Eternity** | Gautam Buddha University

> ⚠️ **Current Status:** This project is in active **development phase**. The team is building core modules and integrating backend services.

---

## 🌐 Project Title

**Revolutionizing Satellite Data Access with an AI Help Bot**

---

## 📌 Problem Statement

> *"AI-based Help Bot for Information Retrieval from a Knowledge Graph Based on Static/Dynamic Web Portal Content (MOSDAC)"*

MOSDAC hosts a vast range of technical documentation and satellite data, but users face:

* Navigation bottlenecks
* Scattered and hard-to-parse information
* Inefficient manual search experiences

---

## 💡 Our Solution

An **AI Help Bot** that:

* Understands queries in natural language
* Leverages a **Knowledge Graph + Vector DB** built from MOSDAC content
* Uses **fine-tuned LLMs** for high-quality responses
* Offers **geospatial intelligence** like mapping queries to satellite visual data
* Works with **multi-turn memory** for sustained conversations

---

## 🎯 Key Features

* **Smart Query Understanding**: NLP + intent recognition
* **Knowledge Graph Search**: Precise entity-level mapping using Neo4j
* **RAG Response Generation**: Combines search + generation for deep accuracy
* **Geo-Spatial Intelligence**: Satellite data & maps rendered contextually
* **Multi-Turn Memory**: Maintains chat history context
* **Fast & Emotion-Aware**: Response latency optimized with vector DB and fine-tuning
* **Low-Cost Deployment**: Using open-source models + inference through **Groq API**
* **Scalable UI**: Built for plug-and-play with similar portals (ISRO/BIS/Meghdoot)

---

## 🛠️ Tech Stack

| Category         | Tools Used                                       |
| ---------------- | ------------------------------------------------ |
| Backend          | Python, FastAPI, Redis, Docker                   |
| ML & LLM         | HuggingFace, LLaMA 3.2/3.3 (fine-tuned), PyTorch |
| Retrieval        | Pinecone (Vector DB), Neo4j (Knowledge Graph)    |
| Data Storage     | MongoDB (Chat logs), NoSQL                       |
| UI & DevOps      | TypeScript, Git, Jenkins, CI/CD, Postman         |
| Cloud Deployment | AWS / Google Cloud, Groq API (LLM inference)     |
| Hardware Support | NVIDIA CUDA (Optional for fine-tuning)           |

---

## 🧱 Project Structure

```
📦 AI-Help-Bot
├── app.py             # Main FastAPI app
├── db_handler.py      # Handles MongoDB connections
├── helper.py          # Pinecone & Neo4j utility functions
├── prompt.py          # Prompt templates and dynamic inputs
├── requirements.txt   # Python dependencies
├── .env               # Environment variables
└── README.md          # This file
```

---

## ⚙️ Setup & Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/isro-ai-help-bot.git
   cd isro-ai-help-bot
   ```

2. **(Optional) Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure `.env`**

   ```env
   MONGO_URI="your_mongodb_uri"
   PINECONE_API_KEY="your_pinecone_api_key"
   NEO4J_URI="your_neo4j_uri"
   GROQ_API_KEY="your_groq_api_key"
   ```

5. **Run the Application**

   ```bash
   uvicorn app:app --reload
   ```

---

## 🧪 Usage Workflow

1. **User** sends a natural language question via UI or API.
2. **RAG System** retrieves and augments data from Neo4j + Pinecone.
3. **LLM** (via Groq or locally) generates a contextual and domain-specific response.
4. **MongoDB** stores the chat for future reference and training feedback loop.

---

## 📊 Future Enhancements

* 🌍 Integrate **map visual rendering** (e.g., show cyclone data over Kerala)
* 🧠 Expand **fine-tuning on space and weather domain**
* 🌐 Build a **public-facing UI** with multilingual support
* 📈 Add **auto-learning** from new MOSDAC updates

---

## 🌟 Unique Selling Points

* 🛰️ **Geospatial-AI Synergy**: Space data meets NLP
* 🧩 **Plug-and-Play Architecture**: Deployable on other portals (e.g., ISRO, BIS)
* 🤖 **Emotion-Aware Responses**: Personalized answer tone
* 💸 **Cost-Optimized**: Uses open-source and Groq API for inference

---

## 🤝 Contributing

Pull requests and ideas are welcome—especially from satellite data, AI, and geospatial communities.

---

## 📜 License

Licensed under the **MIT License**.

---

## 🙌 Acknowledgments

* **Hugging Face** for open-source LLMs
* **Groq** for blazing-fast inference
* **Pinecone** and **Neo4j** for retrieval backends
* **ISRO + MOSDAC** for making scientific data public

---


> 🌠 *"Empowering Bharat’s space data with accessible, intelligent AI conversations."*

