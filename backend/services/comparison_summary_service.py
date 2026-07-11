from llm.comparison_prompt_builder import ComparisonPromptBuilder
from llm.answer_generator import AnswerGenerator


class ComparisonSummaryService:
    """
    Generates an AI-powered summary for
    multiple financial reports.
    """

    def __init__(self):
        self.prompt_builder = ComparisonPromptBuilder()
        self.answer_generator = AnswerGenerator()

    def generate_summary(self, documents):
        """
        Generate a comparison summary.

        Args:
            documents (list): List of selected documents.

        Returns:
            str
        """

        if not documents:

            return "No documents available for comparison."

        prompt = self.prompt_builder.build_prompt(
            documents
        )

        summary = self.answer_generator.generate(
            prompt
        )

        return summary