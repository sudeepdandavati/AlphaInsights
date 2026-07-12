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
from services.document_service import DocumentService
from services.comparison_service import ComparisonService
from services.comparison_service import ComparisonService
from services.insights_service import InsightsService


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

# Multi-document registry
document_service = DocumentService()

comparison_service = ComparisonService()

insights_service = InsightsService()


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
    document_id: str
    top_k: int = 3

class CompareRequest(BaseModel):
    document_ids: List[str]

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

@app.get("/documents")
def get_documents():
    """
    Return all uploaded documents.
    """

    return {
        "documents": document_service.get_documents()
    }

@app.get("/documents/{document_id}/metrics")
def get_document_metrics(document_id: str):
    """
    Return extracted financial metrics for a document.
    """

    document = document_service.get_document(document_id)

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found.",
        )

    return {
        "document_id": document["id"],
        "document_name": document["name"],
        "metrics": document["metrics"],
    }


@app.post("/compare")
def compare_reports(request: CompareRequest):
    """
    Compare multiple uploaded financial reports.
    """

    selected_documents = []

    for document_id in request.document_ids:

        document = document_service.get_document(document_id)

        if document is not None:
            selected_documents.append(document)

    comparison = comparison_service.compare(
        selected_documents
    )

    insights = insights_service.generate_insights(
        selected_documents
    )

    comparison["insights"] = insights

    return comparison


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
        top_k=request.top_k,
        document_id=request.document_id,
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

    # Register the uploaded document
    document_service.register_document(
        document_id=result["document_id"],
        document_name=result["document_name"],
        page_count=result["page_count"],
        chunk_count=result["chunk_count"],
        embedding_count=result["embedding_count"],
        metrics=result["metrics"],
    )

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