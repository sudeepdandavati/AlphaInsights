import fitz


class PDFParser:
    """
    PDF Parser for extracting text and metadata from financial reports.
    """

    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.document = None

    def open_pdf(self):
        """
        Opens the PDF document.
        """
        self.document = fitz.open(self.pdf_path)

    def get_page_count(self):
        """
        Returns the total number of pages.
        """
        if self.document is None:
            raise ValueError("PDF is not opened. Call open_pdf() first.")

        return len(self.document)

    def extract_text(self):
        """
        Extracts text from every page.
        """
        if self.document is None:
            raise ValueError("PDF is not opened. Call open_pdf() first.")

        extracted_text = []

        for page in self.document:
            extracted_text.append(page.get_text())

        return "\n".join(extracted_text)

    def get_metadata(self):
        """
        Returns PDF metadata.
        """
        if self.document is None:
            raise ValueError("PDF is not opened. Call open_pdf() first.")

        return self.document.metadata