# ☕ Brew Haven RAG — Retrieval-Augmented Generation System

**Brew Haven RAG** is an advanced **Retrieval-Augmented Generation (RAG)** system developed for **Brew Haven Coffee**, powered by **Google’s Gemini** for intelligent, context-aware responses.  

This system integrates **LangChain**, **Streamlit**, **Pinecone**, and **NVIDIA Llama embeddings** to deliver grounded, accurate, and conversational AI experiences — enabling Brew Haven’s team and customers to interact naturally with the company’s knowledge base.

---

## 🚀 Overview

**Brew Haven RAG** enhances Gemini’s reasoning capabilities by grounding its responses in Brew Haven’s internal data — including product catalogs, recipes, and operational manuals.  

When a user submits a query:
1. Relevant documents are retrieved from **Pinecone** using **NVIDIA Llama embeddings**.  
2. The **LangChain backend** processes and constructs a retrieval context.  
3. **Google’s Gemini** uses this context to generate factual, data-driven responses.  
4. The **Streamlit frontend** presents the output through an interactive chat interface.

---

## 🧠 Architecture

```
User (Streamlit Interface)
   ↓
LangChain Backend
   ↓
Retriever (Pinecone + Llama Embeddings)
   ↓
Generator (Google Gemini)
   ↓
Contextual Answer
```

---

## ⚙️ Technology Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | Streamlit |
| **Backend** | LangChain |
| **LLM (Generator)** | Google Gemini |
| **Vector Database** | Pinecone |
| **Embeddings** | NVIDIA Llama |
| **Language** | Python 3.11 |
| **Deployment** | Docker & Docker Compose |

---

## ☕ Key Features

- **Gemini-powered contextual generation** tailored for Brew Haven Coffee.  
- **Accurate and real-time retrieval** using **Pinecone**.  
- **High-performance embeddings** via **NVIDIA Llama**.  
- **Clean and interactive interface** built with **Streamlit**.  
- **Modular and scalable backend** structured with **LangChain**.  

---

## 🧑‍💻 Author

**Kevin Wiharja**  
Built with ☕, 💡, and the synergy of **Gemini**, **LangChain**, and **Streamlit**.  
