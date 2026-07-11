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

    def retrieve(
    self,
    question,
    top_k=5,
    document_id=None,
):
        """
        Retrieve the most relevant chunks.
        """

        query_embedding = self.embedding_generator.generate_embedding(question)

        results = self.vector_store.search(
    query_embedding=query_embedding,
    top_k=top_k,
    document_id=document_id,
)

        retrieved_chunks = []

        for point in results:

            payload = point.payload

            retrieved_chunks.append(
                {
                    "score": round(point.score, 4),
                    "document_id": payload.get("document_id"),
                    "document_name": payload.get("document_name"),

                    "chunk_id": payload["chunk_id"],
                    "text": payload["text"],

                    "start": payload["start"],
                    "end": payload["end"],
                    "length": payload["length"],
                }
            )

        return retrieved_chunks