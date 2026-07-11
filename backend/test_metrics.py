from extraction.financial_metrics import FinancialMetricsExtractor

text = """
Revenue $391.0B

Net income $93.7B

Operating income $123.5B

EPS $6.11

Cash and cash equivalents $67.2B
"""

extractor = FinancialMetricsExtractor()

metrics = extractor.extract(text)

print(metrics)