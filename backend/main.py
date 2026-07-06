from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from ingestion.pdf_parser import PDFParser
from retrieval.retriever import Retriever
from llm.prompt_builder import PromptBuilder
from llm.answer_generator import AnswerGenerator


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
    chunk_id: int
    score: float


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
            "chunk_id": chunk["chunk_id"],
            "score": chunk["score"],
        }
        for chunk in chunks
    ]

    return {
        "question": request.question,
        "answer": answer,
        "sources": sources
    }