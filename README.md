# AlphaInsights

AlphaInsights is an AI-powered financial document analysis project that demonstrates how Retrieval-Augmented Generation (RAG) systems are built from the ground up. The project focuses on processing corporate financial reports, generating semantic embeddings, and preparing data for intelligent retrieval and question answering.

The goal of this project is not only to build a working RAG application but also to understand every stage of the pipeline by implementing the core components step by step.

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
- Independent module testing

---

## ✅ Phase 4 – Embedding Generation

Implemented:

- Local embedding generation using **BAAI/bge-small-en-v1.5**
- LangChain embedding integration
- Batch embedding generation
- End-to-end ingestion pipeline
- Embedding pipeline testing

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
Vector Embeddings
```

---

# Project Structure

```
AlphaInsights/

backend/
│
├── embeddings/
│   └── embedding_generator.py
│
├── ingestion/
│   └── pdf_parser.py
│
├── pipelines/
│   └── ingestion_pipeline.py
│
├── preprocessing/
│   ├── text_cleaner.py
│   └── chunker.py
│
├── tests/
│
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

## Frontend

- React
- Vite
- Axios

## AI & Machine Learning

- BAAI/bge-small-en-v1.5
- Hugging Face
- LangChain Embeddings

## Development Tools

- Git
- GitHub
- Docker
- Postman

---

# Current Pipeline

The ingestion pipeline currently performs the following steps:

1. Read a financial PDF
2. Extract the document text
3. Clean and normalize the extracted content
4. Split the document into overlapping chunks
5. Generate semantic embeddings for every chunk

Each chunk is enriched with metadata and converted into a vector representation that will be stored in a vector database during the next phase.

---

# Upcoming Phases

- Vector Database (Qdrant)
- Semantic Retrieval
- Hybrid Search (BM25 + Vector Search)
- Reranking
- LangGraph Agent Workflow
- Financial Question Answering
- Frontend Integration
- Deployment

---

# Why AlphaInsights?

Most RAG tutorials focus on using high-level libraries without explaining what happens internally. AlphaInsights takes a different approach by implementing each stage of the pipeline step by step before integrating production-ready tools.

This project is intended as both a learning experience and a portfolio project that demonstrates practical software engineering, AI integration, and Retrieval-Augmented Generation concepts.

---

# Current Status

**Version:** v0.4

**Status:** Phase 4 – Embedding Generation Completed