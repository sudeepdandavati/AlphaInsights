class Chunker:
    """
    Splits cleaned text into overlapping chunks.
    """

    def __init__(self, chunk_size=1000, chunk_overlap=200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split_text(self, text):
        """
        Split text into overlapping chunks and return metadata.
        """

        chunks = []

        start = 0
        chunk_id = 1

        while start < len(text):

            end = start + self.chunk_size

            chunk_text = text[start:end]

            chunks.append({
                "chunk_id": chunk_id,
                "start": start,
                "end": min(end, len(text)),
                "length": len(chunk_text),
                "text": chunk_text
            })

            chunk_id += 1

            start += self.chunk_size - self.chunk_overlap

        return chunks