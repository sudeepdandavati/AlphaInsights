import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))from ingestion.pdf_parser import PDFParser

pdf_path = "../data/reports/sample report.pdf"

parser = PDFParser(pdf_path)

parser.open_pdf()

print("=" * 60)
print("PDF INFORMATION")
print("=" * 60)

print(f"Total Pages : {parser.get_page_count()}")

print("\nMetadata")
print(parser.get_metadata())

text = parser.extract_text()

print("\nFirst 1000 Characters\n")

print(text[:1000])