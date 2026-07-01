from langchain_huggingface import HuggingFaceEmbeddings


class EmbeddingGenerator:
    """
    Generates vector embeddings for text using HuggingFace models.
    """

    def __init__(self):
        self.model = HuggingFaceEmbeddings(
            model_name="BAAI/bge-small-en-v1.5",
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True},
        )

    def generate_embedding(self, text):
        """
        Generate an embedding for a single text.

        Args:
            text (str): Input text.

        Returns:
            list: Embedding vector.
        """
        return self.model.embed_query(text)

    def generate_embeddings(self, texts):
        """
        Generate embeddings for multiple texts.

        Args:
            texts (list): List of strings.

        Returns:
            list: List of embedding vectors.
        """
        return self.model.embed_documents(texts)