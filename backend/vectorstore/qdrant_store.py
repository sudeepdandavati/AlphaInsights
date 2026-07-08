import uuid

from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct,
)


class QdrantStore:
    """
    Handles all interactions with the Qdrant vector database.
    """

    def __init__(self):
        self.client = QdrantClient(
            host="localhost",
            port=6333,
        )

    def create_collection(self, collection_name="alphainsights"):
        """
        Create a collection if it does not already exist.
        """

        collections = self.client.get_collections().collections

        existing = [collection.name for collection in collections]

        if collection_name not in existing:

            self.client.create_collection(
                collection_name=collection_name,
                vectors_config=VectorParams(
                    size=384,
                    distance=Distance.COSINE,
                ),
            )

            print(f"Collection '{collection_name}' created successfully.")

        else:

            print(f"Collection '{collection_name}' already exists.")

    def upload_documents(
        self,
        chunks,
        embeddings,
        document_name,
        document_id,
        collection_name="alphainsights"
    ):
        """
        Upload chunks and embeddings to Qdrant.
        """

        points = []

        for chunk, embedding in zip(chunks, embeddings):

            points.append(
                PointStruct(
                    id=str(uuid.uuid4()),
                    vector=embedding,
                    payload={
                        "document_id": document_id,
                        "document_name": document_name,

                        "chunk_id": chunk["chunk_id"],
                        "text": chunk["text"],

                        "start": chunk["start"],
                        "end": chunk["end"],
                        "length": chunk["length"],
                    },
                )
            )

        self.client.upsert(
            collection_name=collection_name,
            points=points,
        )

        print(f"Uploaded {len(points)} vectors successfully.")

    def search(
        self,
        query_embedding,
        top_k=5,
        collection_name="alphainsights"
    ):
        """
        Search for the most similar chunks in Qdrant.
        """

        results = self.client.query_points(
            collection_name=collection_name,
            query=query_embedding,
            limit=top_k,
        )

        return results.points