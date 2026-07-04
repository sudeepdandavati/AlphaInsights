import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from pipelines.ingestion_pipeline import IngestionPipeline
from vectorstore.qdrant_store import QdrantStore

pdf_path = "../data/reports/sample report.pdf"

print("=" * 60)
print("DOCUMENT INGESTION")
print("=" * 60)

pipeline = IngestionPipeline()

result = pipeline.process(pdf_path)

store = QdrantStore()

store.create_collection()

store.upload_documents(
    chunks=result["chunks"],
    embeddings=result["embeddings"]
)

print("\nDocument uploaded successfully.")
print(f"Total Chunks : {len(result['chunks'])}")
print(f"Total Vectors: {len(result['embeddings'])}")