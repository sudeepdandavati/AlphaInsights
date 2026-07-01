import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from ingestion.pdf_parser import PDFParser
from preprocessing.text_cleaner import TextCleaner
from preprocessing.chunker import Chunker

pdf_path = "../data/reports/sample report.pdf"

parser = PDFParser(pdf_path)
parser.open_pdf()

raw_text = parser.extract_text()

cleaner = TextCleaner()
clean_text = cleaner.clean_text(raw_text)

chunker = Chunker(chunk_size=1000, chunk_overlap=200)

chunks = chunker.split_text(clean_text)

print("=" * 60)
print("CHUNK INFORMATION")
print("=" * 60)

print(f"Total Chunks : {len(chunks)}")

print("\n")

print("First Chunk Metadata")

print(chunks[0])

print("\n")

print("=" * 60)

print("Second Chunk Metadata")

print(chunks[1])