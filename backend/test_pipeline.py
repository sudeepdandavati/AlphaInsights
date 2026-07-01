from pipelines.ingestion_pipeline import IngestionPipeline

pdf_path = "../data/reports/sample report.pdf"

pipeline = IngestionPipeline()

result = pipeline.process(pdf_path)

print("=" * 60)
print("INGESTION PIPELINE")
print("=" * 60)

print(f"Pages            : {result['page_count']}")
print(f"Chunks           : {len(result['chunks'])}")
print(f"Embeddings       : {len(result['embeddings'])}")
print(f"Embedding Size   : {len(result['embeddings'][0])}")

print("\nMetadata:\n")

print(result["metadata"])

print("\nFirst Chunk:\n")

print(result["chunks"][0]["text"][:300])