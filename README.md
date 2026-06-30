# AlphaInsights

AlphaInsights is a personal project that explores how Retrieval-Augmented Generation (RAG) can be applied to corporate financial analysis. The goal is to build the entire pipeline from scratch, starting with financial document ingestion and gradually adding retrieval, embeddings, vector search, and LLM-powered question answering.

---

## Current Progress

### ✅ Phase 1 - Project Setup

- FastAPI backend
- React + Vite frontend
- Frontend and backend communication
- Swagger API documentation
- GitHub project setup

### ✅ Phase 2 - PDF Ingestion

Implemented:

- Read financial PDF documents
- Extract complete document text
- Extract PDF metadata
- Count document pages
- Expose PDF information through a FastAPI endpoint

### ✅ Phase 3 - Text Preprocessing

Implemented:

- Text cleaning
- Whitespace normalization
- Sliding window chunking
- Configurable chunk size
- Configurable chunk overlap
- Chunk metadata generation
- Independent testing for preprocessing pipeline

---

## Project Structure

```text
AlphaInsights/

backend/
├── ingestion/
│   └── pdf_parser.py
│
├── preprocessing/
│   ├── text_cleaner.py
│   └── chunker.py
│
├── models/
├── utils/
├── main.py

frontend/

data/
└── reports/

docs/
```

---

## Technologies

### Backend

- FastAPI
- Python
- PyMuPDF
- pdfplumber

### Frontend

- React
- Vite
- Axios

### Development

- Git
- GitHub

---

## Upcoming Phases

- Embedding Generation
- Qdrant Vector Database
- Hybrid Retrieval
- LangGraph Workflow
- Local LLM Integration (Ollama)
- Financial Question Answering
- Deployment

---

## Why this project?

Financial reports contain large amounts of structured and unstructured information. AlphaInsights aims to build a complete RAG pipeline capable of understanding these documents and answering financial questions with relevant supporting context.

The project focuses on understanding each stage of the RAG pipeline rather than relying entirely on high-level frameworks.

---

## Current Status

**Version:** v0.3

**Status:** Phase 3 – Text Preprocessing Completed