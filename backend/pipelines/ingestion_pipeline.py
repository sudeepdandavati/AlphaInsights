from ingestion.pdf_parser import PDFParser
from preprocessing.text_cleaner import TextCleaner
from preprocessing.chunker import Chunker
from embeddings.embedding_generator import EmbeddingGenerator


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

    def process(self, pdf_path):
        """
        Process a PDF from start to finish.

        Returns:
            dict
        """

        # Step 1: Parse PDF
        parser = PDFParser(pdf_path)
        parser.open_pdf()

        raw_text = parser.extract_text()

        # Step 2: Clean text
        clean_text = self.cleaner.clean_text(raw_text)

        # Step 3: Chunk text
        chunks = self.chunker.split_text(clean_text)

        # Step 4: Extract chunk texts
        chunk_texts = [chunk["text"] for chunk in chunks]

        # Step 5: Generate embeddings
        embeddings = self.embedding_generator.generate_embeddings(chunk_texts)

        return {
            "chunks": chunks,
            "embeddings": embeddings,
            "metadata": parser.get_metadata(),
            "page_count": parser.get_page_count()
        }