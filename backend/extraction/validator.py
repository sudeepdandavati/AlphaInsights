from extraction.number_parser import NumberParser


class MetricValidator:
    """
    Validates extracted financial metrics.

    Ensures that invalid or malformed values
    are rejected before they are stored or displayed.
    """

    @staticmethod
    def validate(metric_name, value):
        """
        Validate a single financial metric.

        Args:
            metric_name (str)
            value (str | int | float)

        Returns:
            int | float | None
        """

        parsed_value = NumberParser.parse(value)

        if parsed_value is None:
            return None

        # Financial metrics should never be negative
        # except in rare accounting situations.
        # For now, reject negatives.
        if parsed_value < 0:
            return None

        return parsed_value

    @staticmethod
    def validate_metrics(metrics):
        """
        Validate an entire metrics dictionary.

        Args:
            metrics (dict)

        Returns:
            dict
        """

        validated = {}

        for metric_name, value in metrics.items():

            validated[metric_name] = MetricValidator.validate(
                metric_name,
                value,
            )

        return validated