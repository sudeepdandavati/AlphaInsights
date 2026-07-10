from pathlib import Path
import shutil
from typing import List

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from ingestion.pdf_parser import PDFParser
from retrieval.retriever import Retriever
from llm.prompt_builder import PromptBuilder
from llm.answer_generator import AnswerGenerator
from pipelines.ingestion_pipeline import IngestionPipeline


app = FastAPI(
    title="AlphaInsights API",
    version="1.0.0"
)


# -------------------------------------------------
# Create reusable instances
# -------------------------------------------------

retriever = Retriever()
prompt_builder = PromptBuilder()
answer_generator = AnswerGenerator()
ingestion_pipeline = IngestionPipeline()


# -------------------------------------------------
# Upload Configuration
# -------------------------------------------------

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


# -------------------------------------------------
# Request & Response Models
# -------------------------------------------------

class SearchRequest(BaseModel):
    question: str
    top_k: int = 5


class SearchResult(BaseModel):
    score: float
    chunk_id: int
    text: str
    start: int
    end: int
    length: int


class SearchResponse(BaseModel):
    question: str
    results: List[SearchResult]


class AskRequest(BaseModel):
    question: str
    top_k: int = 3


class Source(BaseModel):
    document_name: str

    chunk_id: int
    score: float
    text: str


class AskResponse(BaseModel):
    question: str
    answer: str
    sources: List[Source]


# -------------------------------------------------
# Allow React Frontend
# -------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------------------------------------------------
# API Endpoints
# -------------------------------------------------

@app.get("/")
def root():
    return {
        "message": "Welcome to AlphaInsights 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/pdf-info")
def pdf_info():

    pdf_path = "../data/reports/sample report.pdf"

    parser = PDFParser(pdf_path)

    parser.open_pdf()

    return {
        "pages": parser.get_page_count(),
        "metadata": parser.get_metadata()
    }


@app.post("/search", response_model=SearchResponse)
def search(request: SearchRequest):
    """
    Retrieve the most relevant document chunks.
    """

    results = retriever.retrieve(
        question=request.question,
        top_k=request.top_k
    )

    return {
        "question": request.question,
        "results": results
    }


@app.post("/ask", response_model=AskResponse)
def ask(request: AskRequest):
    """
    Retrieve relevant context and generate an answer using the LLM.
    """

    # Retrieve relevant chunks
    chunks = retriever.retrieve(
        question=request.question,
        top_k=request.top_k
    )

    # Build prompt
    prompt = prompt_builder.build_prompt(
        question=request.question,
        retrieved_chunks=chunks
    )

    # Generate answer
    answer = answer_generator.generate(prompt)

    # Build source list
    sources = [
        {
            "document_name": chunk["document_name"],

            "chunk_id": chunk["chunk_id"],
            "score": chunk["score"],
            "text": chunk["text"],
        }
        for chunk in chunks
    ]

    return {
        "question": request.question,
        "answer": answer,
        "sources": sources,
    }


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF, process it, generate embeddings,
    and store everything in Qdrant.
    """

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Process the uploaded document
    result = ingestion_pipeline.process(str(file_path))

    return {
        "message": "Document uploaded and indexed successfully.",
        "document": {
            "id": result["document_id"],
            "name": result["document_name"],
        },
        "pages": result["page_count"],
        "chunks": result["chunk_count"],
        "embeddings": result["embedding_count"],
    }