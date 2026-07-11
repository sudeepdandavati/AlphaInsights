from services.comparison_summary_service import ComparisonSummaryService


class ComparisonService:
    """
    Handles comparison of multiple financial reports.

    Returns both the comparison data and
    an AI-generated financial summary.
    """

    def __init__(self):
        self.summary_service = ComparisonSummaryService()

    def compare(self, documents):
        """
        Compare the selected financial reports.

        Args:
            documents (list): Selected documents.

        Returns:
            dict
        """

        comparison = {
            "documents": []
        }

        for document in documents:

            comparison["documents"].append(
                {
                    "id": document["id"],
                    "name": document["name"],
                    "metrics": document["metrics"],
                }
            )

        # ----------------------------------------
        # Generate AI Summary
        # ----------------------------------------

        summary = self.summary_service.generate_summary(
            documents
        )

        comparison["summary"] = summary

        return comparison