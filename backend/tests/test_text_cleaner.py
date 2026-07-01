import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from ingestion.pdf_parser import PDFParser
from preprocessing.text_cleaner import TextCleaner

# Path to the sample PDF
pdf_path = "../data/reports/sample report.pdf"

# Step 1: Extract raw text
parser = PDFParser(pdf_path)
parser.open_pdf()
raw_text = parser.extract_text()

# Step 2: Clean the text
cleaner = TextCleaner()
clean_text = cleaner.clean_text(raw_text)

# Display results
print("=" * 60)
print("RAW TEXT PREVIEW")
print("=" * 60)
print(raw_text[:1000])

print("\n")

print("=" * 60)
print("CLEANED TEXT PREVIEW")
print("=" * 60)
print(clean_text[:1000])