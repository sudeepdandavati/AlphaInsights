import re


class TextCleaner:
    """
    Cleans and normalizes extracted PDF text.
    """

    def clean_text(self, text):
        """
        Cleans the extracted text by removing unnecessary whitespace.

        Args:
            text (str): Raw extracted text.

        Returns:
            str: Cleaned text.
        """

        # Replace multiple spaces/tabs with a single space
        text = re.sub(r"[ \t]+", " ", text)

        # Replace multiple blank lines with a single blank line
        text = re.sub(r"\n\s*\n+", "\n\n", text)

        # Remove leading and trailing whitespace
        text = text.strip()

        return text