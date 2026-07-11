class ComparisonPromptBuilder:
    """
    Builds prompts for AI-powered comparison
    of multiple financial reports.
    """

    def build_prompt(self, documents):
        """
        Build a prompt for comparing multiple
        financial reports.

        Args:
            documents (list): List of documents with metrics.

        Returns:
            str
        """

        prompt = """
You are an expert financial analyst.

Compare the following financial reports using ONLY the provided financial metrics.

Generate a concise comparison summary.

Requirements:

- Highlight which company has the highest revenue.
- Highlight which company has the highest net income.
- Highlight which company has the highest EPS.
- Highlight which company appears strongest financially.
- Mention any missing financial information.
- Keep the summary between 5 and 8 bullet points.
- Do NOT invent numbers.
- Only use the provided metrics.

Financial Reports:

"""

        for document in documents:

            metrics = document["metrics"]

            prompt += f"""
Company: {document["name"]}

Revenue: {metrics.get("revenue")}
Net Income: {metrics.get("net_income")}
Gross Profit: {metrics.get("gross_profit")}
Operating Income: {metrics.get("operating_income")}
EPS: {metrics.get("eps")}
Cash: {metrics.get("cash")}
Total Assets: {metrics.get("total_assets")}
Total Liabilities: {metrics.get("total_liabilities")}
Total Debt: {metrics.get("total_debt")}

--------------------------------------------

"""

        prompt += """

Produce a professional financial comparison.

"""

        return prompt