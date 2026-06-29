from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ingestion.pdf_parser import PDFParser

app = FastAPI(
    title="AlphaInsights API",
    version="1.0.0"
)

# Allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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