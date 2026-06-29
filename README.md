# AlphaInsights

AlphaInsights is a personal project that explores how Retrieval-Augmented Generation (RAG) can be applied to corporate financial analysis. The goal is to build the entire pipeline from scratch, starting with financial document ingestion and gradually adding retrieval, embeddings, vector search, and LLM-powered question answering.

Instead of relying on high-level frameworks to hide the implementation details, this project focuses on understanding how each component works and how they fit together in a production-style RAG system.

---

## Current Progress

### ✅ Phase 1 - Project Setup

* FastAPI backend
* React + Vite frontend
* Frontend and backend communication
* Swagger API documentation
* GitHub project setup

### ✅ Phase 2 - PDF Ingestion

Currently implemented:

* Read financial PDF documents
* Extract document text
* Extract PDF metadata
* Count document pages
* Expose PDF information through a FastAPI endpoint

Example endpoint:

```
GET /pdf-info
```

---

## Project Structure

```
AlphaInsights/

backend/
├── ingestion/
│   └── pdf_parser.py
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

* FastAPI
* Python
* PyMuPDF
* pdfplumber

### Frontend

* React
* Vite
* Axios

### Development

* Git
* GitHub

---

## Planned Features

The project will continue to evolve with the following components:

* Text preprocessing
* Intelligent document chunking
* Metadata enrichment
* Embedding generation
* Qdrant vector database
* Hybrid search
* Reranking
* LangGraph workflow
* Local LLM integration using Ollama
* Financial question answering

---

## Why this project?

Financial reports contain large amounts of structured and unstructured information. The objective of AlphaInsights is to build a system that can process these reports and answer financial questions with relevant supporting context.

The project is also intended as a hands-on way to understand how modern RAG systems are designed beyond simple chatbot examples.

---

## Current Status

**Version:** 0.2

**Status:** PDF ingestion pipeline completed.
