class InsightsPromptBuilder:
    """
    Builds prompts for generating AI-powered
    financial insights from multiple reports.
    """

    def build_prompt(self, documents):
        """
        Build the prompt for the LLM.

        Args:
            documents (list)

        Returns:
            str
        """

        prompt = """
You are a senior financial analyst.

Analyze the following companies using ONLY the provided financial metrics.

Requirements:

- Produce 5 to 8 concise bullet points.
- Compare companies objectively.
- Mention strengths and weaknesses.
- Highlight profitability.
- Highlight liquidity.
- Highlight debt levels.
- Mention missing financial data if applicable.
- Do not invent any numbers.
- Do not speculate beyond the provided metrics.

Financial Reports

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

----------------------------------------

"""

        prompt += """

Generate professional financial insights.

"""

        return prompt