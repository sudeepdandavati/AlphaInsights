from pathlib import Path
import uuid

from ingestion.pdf_parser import PDFParser
from preprocessing.text_cleaner import TextCleaner
from preprocessing.chunker import Chunker
from embeddings.embedding_generator import EmbeddingGenerator
from vectorstore.qdrant_store import QdrantStore


class IngestionPipeline:
    """
    End-to-end pipeline for processing financial PDF reports.
    """

    def __init__(self):
        self.cleaner = TextCleaner()

        self.chunker = Chunker(
            chunk_size=1000,
            chunk_overlap=200
        )

        self.embedding_generator = EmbeddingGenerator()

        self.vector_store = QdrantStore()

    def process(self, pdf_path):
        """
        Process a PDF from start to finish.

        Returns:
            dict
        """

        # -----------------------------------------
        # Document Metadata
        # -----------------------------------------

        document_name = Path(pdf_path).name
        document_id = str(uuid.uuid4())

        # -----------------------------------------
        # Step 1: Parse PDF
        # -----------------------------------------

        parser = PDFParser(pdf_path)
        parser.open_pdf()

        raw_text = parser.extract_text()

        # -----------------------------------------
        # Step 2: Clean text
        # -----------------------------------------

        clean_text = self.cleaner.clean_text(raw_text)

        # -----------------------------------------
        # Step 3: Chunk text
        # -----------------------------------------

        chunks = self.chunker.split_text(clean_text)

        # -----------------------------------------
        # Step 4: Generate Embeddings
        # -----------------------------------------

        chunk_texts = [
            chunk["text"]
            for chunk in chunks
        ]

        embeddings = self.embedding_generator.generate_embeddings(
            chunk_texts
        )

        # -----------------------------------------
        # Step 5: Store in Qdrant
        # -----------------------------------------

        self.vector_store.create_collection()

        self.vector_store.upload_documents(
            chunks=chunks,
            embeddings=embeddings,
            document_name=document_name,
            document_id=document_id,
        )

        # -----------------------------------------
        # Return Statistics
        # -----------------------------------------

        return {
            "document_id": document_id,
            "document_name": document_name,
            "page_count": parser.get_page_count(),
            "chunk_count": len(chunks),
            "embedding_count": len(embeddings),
            "metadata": parser.get_metadata(),
        }