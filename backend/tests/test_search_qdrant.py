import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from embeddings.embedding_generator import EmbeddingGenerator
from vectorstore.qdrant_store import QdrantStore

print("=" * 60)
print("SEMANTIC SEARCH")
print("=" * 60)

question = "What was Apple's revenue in 2024?"

embedding_model = EmbeddingGenerator()

query_embedding = embedding_model.generate_embedding(question)

store = QdrantStore()

results = store.search(
    query_embedding=query_embedding,
    top_k=3,
)

for i, point in enumerate(results, start=1):

    print(f"\nResult {i}")
    print("-" * 40)
    print(f"Score : {point.score:.4f}\n")

    print(point.payload["text"][:500])