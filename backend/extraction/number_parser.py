import re


class NumberParser:
    """
    Parses and normalizes financial numbers.

    Examples:

    "391,035"        -> 391035
    "67.2B"          -> 67200000000
    "2.5M"           -> 2500000
    "120K"           -> 120000
    "."              -> None
    ","              -> None
    "-"              -> None
    "N/A"            -> None
    "4,"             -> None
    """

    INVALID_VALUES = {
        "",
        ".",
        ",",
        "-",
        "--",
        "N/A",
        "NA",
        "None",
        "null",
    }

    MULTIPLIERS = {
        "K": 1_000,
        "M": 1_000_000,
        "B": 1_000_000_000,
        "T": 1_000_000_000_000,
    }

    @classmethod
    def parse(cls, value):
        """
        Convert a financial string into a numeric value.

        Returns:
            float | int | None
        """

        if value is None:
            return None

        value = str(value).strip()

        if value in cls.INVALID_VALUES:
            return None

        # Remove currency symbols
        value = (
            value.replace("$", "")
                 .replace("€", "")
                 .replace("£", "")
                 .strip()
        )

        # Reject incomplete values
        if value.endswith(",") or value.endswith("."):
            return None

        # Match values like:
        # 391,035
        # 67.2B
        # 120M
        # 5.5K
        match = re.match(
            r"^([\d,]+(?:\.\d+)?)([KMBT]?)$",
            value,
            re.IGNORECASE,
        )

        if not match:
            return None

        number = match.group(1).replace(",", "")
        suffix = match.group(2).upper()

        try:
            number = float(number)
        except ValueError:
            return None

        if suffix in cls.MULTIPLIERS:
            number *= cls.MULTIPLIERS[suffix]

        # Return int when possible
        if number.is_integer():
            return int(number)

        return round(number, 2)