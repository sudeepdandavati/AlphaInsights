# AlphaInsights

AlphaInsights is an AI-powered financial document analysis platform that demonstrates how Retrieval-Augmented Generation (RAG) systems are built from the ground up. The project processes corporate financial reports, generates semantic embeddings, stores them in a vector database, retrieves relevant information through semantic search, and uses a local Large Language Model (LLM) to generate accurate, context-aware answers.

The goal of this project is to understand and implement every stage of a modern RAG pipeline while following clean software engineering practices and a modular architecture.

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
- Sentence Transformers integration
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

## ✅ Phase 6 – Retrieval Layer

Implemented:

- Production-ready Retriever module
- Retrieval abstraction
- Clean retrieval response objects
- FastAPI semantic search endpoint (`/search`)
- Structured API responses

---

## ✅ Phase 7 – Local LLM-powered RAG Pipeline

Implemented:

- Ollama integration
- Llama 3.2 local model
- Prompt Builder
- Answer Generator
- End-to-end Retrieval-Augmented Generation (RAG)
- FastAPI `/ask` endpoint
- Source-aware AI responses

---

# Project Architecture

```text
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
Retriever
      │
      ▼
Prompt Builder
      │
      ▼
Ollama (Llama 3.2)
      │
      ▼
Generated Answer
      │
      ▼
FastAPI API
```

---

# Project Structure

```text
AlphaInsights/

backend/
│
├── embeddings/
├── ingestion/
├── llm/
├── pipelines/
├── preprocessing/
├── retrieval/
├── tests/
├── vectorstore/
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

## AI & Machine Learning

- BAAI/bge-small-en-v1.5
- Sentence Transformers
- Ollama
- Llama 3.2

## Vector Database

- Qdrant
- Docker

## Frontend

- React
- Vite
- Axios

## Development Tools

- Git
- GitHub
- Docker
- Swagger UI

---

# Running Qdrant

Start the vector database:

```bash
docker run -d \
  --name alphainsights-qdrant \
  -p 6333:6333 \
  -p 6334:6334 \
  qdrant/qdrant
```

Verify:

```bash
docker ps
```

---

# Running Ollama

Download the model:

```bash
ollama pull llama3.2
```

Start the model:

```bash
ollama run llama3.2
```

---

# Running the Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Search

```
POST /search
```

Returns the most relevant document chunks from Qdrant.

---

## Ask

```
POST /ask
```

Runs the complete Retrieval-Augmented Generation (RAG) pipeline and returns:

- AI-generated answer
- Supporting source chunks

---

# Current Pipeline

The current workflow performs the following steps:

1. Read a financial PDF
2. Extract document text
3. Clean and normalize the content
4. Split the document into overlapping chunks
5. Generate semantic embeddings
6. Store embeddings in Qdrant
7. Retrieve relevant chunks
8. Build an LLM prompt
9. Generate an answer using Ollama (Llama 3.2)
10. Return the answer with supporting sources

---

# Running Tests

```bash
python tests/test_pipeline.py

python tests/test_search_qdrant.py

python tests/test_retriever.py

python tests/test_llm.py
```

---

# Upcoming Phases

- React Chat Interface
- Conversation History
- Hybrid Search (Vector + Keyword)
- Multi-document Support
- Streaming Responses
- Deployment
- Authentication

---

# Why AlphaInsights?

Many RAG tutorials rely heavily on high-level libraries without explaining how the individual components work together.

AlphaInsights takes a step-by-step approach by implementing every stage of the pipeline—from PDF ingestion to AI-generated answers—while maintaining a modular, production-oriented architecture.

The project serves as both a learning experience and a portfolio project demonstrating practical skills in AI engineering, backend development, vector databases, Retrieval-Augmented Generation (RAG), and LLM integration.

---

# Current Status

**Version:** v0.7

**Status:** ✅ Phase 7 – Local LLM-powered RAG Pipeline Completed