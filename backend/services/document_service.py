class DocumentService:
    """
    Stores uploaded document metadata in memory.

    Later this can be replaced with a database.
    """

    def __init__(self):
        self.documents = []

    def register_document(
        self,
        document_id,
        document_name,
        page_count,
        chunk_count,
        embedding_count,
        metrics,
    ):
        """
        Register a newly uploaded document.
        """

        document = {
            "id": document_id,
            "name": document_name,
            "pages": page_count,
            "chunks": chunk_count,
            "embeddings": embedding_count,
            "metrics": metrics,
        }

        # Avoid duplicate registrations
        self.documents = [
            doc for doc in self.documents
            if doc["id"] != document_id
        ]

        self.documents.append(document)

        return document

    def get_documents(self):
        """
        Return all uploaded documents.
        """

        return self.documents

    def get_document(self, document_id):
        """
        Return a single document by ID.
        """

        for document in self.documents:

            if document["id"] == document_id:
                return document

        return None