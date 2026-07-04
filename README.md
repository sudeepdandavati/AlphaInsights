# AlphaInsights

AlphaInsights is an AI-powered financial document analysis project that demonstrates how Retrieval-Augmented Generation (RAG) systems are built from the ground up. The project focuses on processing corporate financial reports, generating semantic embeddings, storing them in a vector database, and retrieving relevant information through semantic search.

The goal of this project is to understand and implement each stage of a modern RAG pipeline while following clean software engineering practices.

---

# Current Progress

## ✅ Phase 1 – Full Stack Foundation

Implemented:

- FastAPI backend
- React + Vite frontend
- Backend and frontend integration
- REST API endpoints
- Swagger documentation
- GitHub project setup

---

## ✅ Phase 2 – PDF Ingestion

Implemented:

- PDF parsing using PyMuPDF
- Text extraction
- PDF metadata extraction
- Page count extraction
- FastAPI integration for PDF information

---

## ✅ Phase 3 – Text Preprocessing

Implemented:

- Text cleaning
- Whitespace normalization
- Sliding window chunking
- Configurable chunk size
- Configurable chunk overlap
- Chunk metadata generation

---

## ✅ Phase 4 – Embedding Generation

Implemented:

- Local embedding generation using BAAI/bge-small-en-v1.5
- LangChain embedding integration
- Batch embedding generation
- End-to-end ingestion pipeline

---

## ✅ Phase 5 – Vector Database & Semantic Search

Implemented:

- Docker-based Qdrant setup
- Qdrant client integration
- Vector collection creation
- Uploading document embeddings
- Payload storage with chunk metadata
- Semantic similarity search
- Separate ingestion and search workflows

---

# Project Architecture

```
Financial PDF
      │
      ▼
PDF Parser
      │
      ▼
Text Cleaner
      │
      ▼
Chunk Generator
      │
      ▼
Embedding Generator
      │
      ▼
Qdrant Vector Database
      │
      ▼
Semantic Search
```

---

# Project Structure

```
AlphaInsights/

backend/
│
├── embeddings/
├── ingestion/
├── pipelines/
├── preprocessing/
├── vectorstore/
├── tests/
├── main.py
└── requirements.txt

frontend/

data/
└── reports/

docs/

README.md
```

---

# Technologies Used

## Backend

- Python 3.11
- FastAPI
- LangChain
- Sentence Transformers
- PyMuPDF
- pdfplumber
- Qdrant Client

## Frontend

- React
- Vite
- Axios

## AI & Machine Learning

- BAAI/bge-small-en-v1.5
- Hugging Face
- LangChain Embeddings

## Database

- Qdrant
- Docker

## Development Tools

- Git
- GitHub
- Docker
- Postman

---

# Current Pipeline

The current workflow performs the following steps:

1. Read a financial PDF
2. Extract document text
3. Clean and normalize the content
4. Split the document into overlapping chunks
5. Generate semantic embeddings
6. Store embeddings in Qdrant
7. Retrieve relevant chunks using semantic similarity search

---

# Upcoming Phases

- Retrieval Layer
- Hybrid Search (Vector + BM25)
- LLM Integration
- Financial Question Answering
- Frontend Integration
- Deployment

---

# Why AlphaInsights?

Many RAG tutorials rely heavily on high-level libraries without explaining how the individual components work together. AlphaInsights takes a step-by-step approach, implementing each stage of the pipeline while maintaining a modular and production-oriented architecture.

The project is designed as both a learning experience and a portfolio project that demonstrates practical skills in AI engineering, backend development, vector databases, and Retrieval-Augmented Generation.

---

# Current Status

**Version:** v0.5

**Status:** Phase 5 – Vector Database & Semantic Search Completed