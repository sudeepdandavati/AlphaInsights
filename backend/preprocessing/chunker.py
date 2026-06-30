class Chunker:
    """
    Splits text using recursive separators before falling back
    to character-based chunking.
    """

    def __init__(self, chunk_size=1000, chunk_overlap=200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split_text(self, text):

        separators = [
            "\n\n",   # Paragraph
            "\n",     # Line
            ". ",     # Sentence
            " ",      # Word
            ""        # Character
        ]

        return self._recursive_split(text, separators)

    def _recursive_split(self, text, separators):

        if len(text) <= self.chunk_size:
            return [{
                "chunk_id": 1,
                "start": 0,
                "end": len(text),
                "length": len(text),
                "text": text
            }]

        separator = separators[0]

        if separator == "":
            return self._character_split(text)

        pieces = text.split(separator)

        if len(pieces) == 1:
            return self._recursive_split(text, separators[1:])

        chunks = []

        current = ""

        chunk_id = 1

        for piece in pieces:

            candidate = current + separator + piece if current else piece

            if len(candidate) <= self.chunk_size:

                current = candidate

            else:

                chunks.append({
                    "chunk_id": chunk_id,
                    "start": 0,
                    "end": len(current),
                    "length": len(current),
                    "text": current
                })

                chunk_id += 1

                current = piece

        if current:

            chunks.append({
                "chunk_id": chunk_id,
                "start": 0,
                "end": len(current),
                "length": len(current),
                "text": current
            })

        return chunks

    def _character_split(self, text):

        chunks = []

        start = 0

        chunk_id = 1

        while start < len(text):

            end = start + self.chunk_size

            chunk = text[start:end]

            chunks.append({
                "chunk_id": chunk_id,
                "start": start,
                "end": min(end, len(text)),
                "length": len(chunk),
                "text": chunk
            })

            chunk_id += 1

            start += self.chunk_size - self.chunk_overlap

        return chunks