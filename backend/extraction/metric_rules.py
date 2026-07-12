class MetricRules:
    """
    Scoring rules for different financial metrics.

    Each metric can have its own strategy for selecting
    the most likely numeric value from a row.
    """

    LARGE_VALUE_METRICS = {
        "revenue",
        "net_income",
        "gross_profit",
        "operating_income",
        "cash",
        "total_assets",
        "total_liabilities",
        "total_debt",
    }

    SMALL_DECIMAL_METRICS = {
        "eps",
    }

    @classmethod
    def score(cls, metric_name, numeric_value):
        """
        Score a candidate value.

        Higher score = more likely to be correct.
        """

        # ----------------------------------------
        # EPS
        # ----------------------------------------

        if metric_name in cls.SMALL_DECIMAL_METRICS:

            if 0 <= numeric_value <= 100:

                return 1_000_000 + numeric_value

            return -1

        # ----------------------------------------
        # Revenue / Assets / Debt / etc.
        # ----------------------------------------

        if metric_name in cls.LARGE_VALUE_METRICS:

            if numeric_value < 100:

                return -1

            return numeric_value

        # ----------------------------------------
        # Default
        # ----------------------------------------

        return numeric_value