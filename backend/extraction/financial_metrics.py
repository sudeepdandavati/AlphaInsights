import re


class FinancialMetricsExtractor:
    """
    Extracts key financial metrics from a financial report.

    This is a rule-based implementation that can later be
    replaced or enhanced with an LLM.
    """

    METRIC_PATTERNS = {
        "revenue": r"(?:Revenue|Net sales)\s*[:\-]?\s*\$?\s*([\d,\.]+\s?[MBTK]?)",
        "net_income": r"(?:Net income|Net earnings)\s*[:\-]?\s*\$?\s*([\d,\.]+\s?[MBTK]?)",
        "gross_profit": r"(?:Gross profit)\s*[:\-]?\s*\$?\s*([\d,\.]+\s?[MBTK]?)",
        "operating_income": r"(?:Operating income)\s*[:\-]?\s*\$?\s*([\d,\.]+\s?[MBTK]?)",
        "eps": r"(?:EPS|Earnings per share)\s*[:\-]?\$?\s*([\d\.]+)",
        "cash": r"(?:Cash(?: and cash equivalents)?)\s*[:\-]?\s*\$?\s*([\d,\.]+\s?[MBTK]?)",
        "total_assets": r"(?:Total assets)\s*[:\-]?\s*\$?\s*([\d,\.]+\s?[MBTK]?)",
        "total_liabilities": r"(?:Total liabilities)\s*[:\-]?\s*\$?\s*([\d,\.]+\s?[MBTK]?)",
        "total_debt": r"(?:Total debt)\s*[:\-]?\s*\$?\s*([\d,\.]+\s?[MBTK]?)",
    }

    def extract(self, text: str) -> dict:
        """
        Extract financial metrics from text.

        Returns:
            dict containing extracted metrics.
        """

        metrics = {}

        for metric, pattern in self.METRIC_PATTERNS.items():

            match = re.search(
                pattern,
                text,
                flags=re.IGNORECASE,
            )

            metrics[metric] = (
                match.group(1).strip()
                if match
                else None
            )

        return metrics