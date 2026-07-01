from embeddings.embedding_generator import EmbeddingGenerator

generator = EmbeddingGenerator()

text = "Apple reported record revenue driven by iPhone sales."

embedding = generator.generate_embedding(text)

print("=" * 60)
print("Embedding Information")
print("=" * 60)

print(f"Vector Dimension : {len(embedding)}")

print("\nFirst 10 Values:\n")

print(embedding[:10])