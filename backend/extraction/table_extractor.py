import fitz


class TableExtractor:
    """
    Extract tables from a PDF using PyMuPDF.

    Returns table contents as plain text so they can
    be searched by the FinancialMetricsExtractor.
    """

    def extract_tables(self, pdf_path):
        """
        Extract all tables from a PDF.

        Args:
            pdf_path (str)

        Returns:
            list[str]
        """

        document = fitz.open(pdf_path)

        tables = []

        for page in document:

            try:

                found_tables = page.find_tables()

                if not found_tables.tables:
                    continue

                for table in found_tables.tables:

                    rows = table.extract()

                    text = "\n".join(

                        " | ".join(
                            str(cell) if cell is not None else ""
                            for cell in row
                        )

                        for row in rows

                    )

                    tables.append(text)

            except Exception:

                # Skip pages that do not contain tables
                continue

        document.close()

        return tables