from embeddings.embedding_generator import EmbeddingGenerator
from vectorstore.qdrant_store import QdrantStore


class Retriever:
    """
    Retrieves the most relevant document chunks
    for a user query.
    """

    def __init__(self):
        self.embedding_generator = EmbeddingGenerator()
        self.vector_store = QdrantStore()

    def retrieve(self, question, top_k=5):
        """
        Retrieve the most relevant chunks.

        Args:
            question (str): User question
            top_k (int): Number of results

        Returns:
            List[dict]: Retrieved chunks with metadata
        """

        query_embedding = self.embedding_generator.generate_embedding(question)

        results = self.vector_store.search(
            query_embedding=query_embedding,
            top_k=top_k,
        )

        retrieved_chunks = []

        for point in results:

            retrieved_chunks.append(
                {
                    "score": round(point.score, 4),
                    "chunk_id": point.payload["chunk_id"],
                    "text": point.payload["text"],
                    "start": point.payload["start"],
                    "end": point.payload["end"],
                    "length": point.payload["length"],
                }
            )

        return retrieved_chunks