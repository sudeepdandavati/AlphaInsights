from ingestion.pdf_parser import PDFParser
from preprocessing.text_cleaner import TextCleaner
from preprocessing.chunker import Chunker
from embeddings.embedding_generator import EmbeddingGenerator

# PDF Path
pdf_path = "../data/reports/sample report.pdf"

# -------------------------------
# Step 1: Parse PDF
# -------------------------------
parser = PDFParser(pdf_path)
parser.open_pdf()

raw_text = parser.extract_text()

# -------------------------------
# Step 2: Clean Text
# -------------------------------
cleaner = TextCleaner()
clean_text = cleaner.clean_text(raw_text)

# -------------------------------
# Step 3: Chunk Text
# -------------------------------
chunker = Chunker(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = chunker.split_text(clean_text)

# Extract only the text from each chunk
chunk_texts = [chunk["text"] for chunk in chunks]

# -------------------------------
# Step 4: Generate Embeddings
# -------------------------------
generator = EmbeddingGenerator()

embeddings = generator.generate_embeddings(chunk_texts)

# -------------------------------
# Results
# -------------------------------
print("=" * 60)
print("DOCUMENT EMBEDDING PIPELINE")
print("=" * 60)

print(f"Total Chunks       : {len(chunks)}")
print(f"Total Embeddings   : {len(embeddings)}")
print(f"Embedding Dimension: {len(embeddings[0])}")

print("\nFirst Chunk Preview:\n")
print(chunk_texts[0][:300])

print("\nFirst Embedding (First 10 Values):\n")
print(embeddings[0][:10])