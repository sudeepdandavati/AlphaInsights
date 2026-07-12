from llm.insights_prompt_builder import InsightsPromptBuilder
from llm.answer_generator import AnswerGenerator


class InsightsService:
    """
    Generates AI-powered financial insights
    for multiple financial reports.
    """

    def __init__(self):
        self.prompt_builder = InsightsPromptBuilder()
        self.answer_generator = AnswerGenerator()

    def generate_insights(self, documents):
        """
        Generate financial insights.

        Args:
            documents (list)

        Returns:
            str
        """

        if not documents:

            return "No financial reports available."

        prompt = self.prompt_builder.build_prompt(
            documents
        )

        insights = self.answer_generator.generate(
            prompt
        )

        return insights