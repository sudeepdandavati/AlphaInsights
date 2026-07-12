import re


class UnitDetector:
    """
    Detects the monetary unit used in a financial report.

    Examples:

    "Amounts in millions"
    "Figures in billions"
    "USD in thousands"
    "(All amounts in millions)"
    """

    UNIT_MULTIPLIERS = {
        "thousand": 1_000,
        "thousands": 1_000,

        "million": 1_000_000,
        "millions": 1_000_000,

        "billion": 1_000_000_000,
        "billions": 1_000_000_000,

        "trillion": 1_000_000_000_000,
        "trillions": 1_000_000_000_000,
    }

    def detect(self, text):
        """
        Detect the reporting unit.

        Returns
        -------
        dict

        {
            "unit": "millions",
            "multiplier": 1000000
        }
        """

        if not text:

            return {
                "unit": None,
                "multiplier": 1,
            }

        # Only inspect the beginning of the document.
        # Reporting units are almost always declared there.
        header = "\n".join(
            text.splitlines()[:250]
        )

        patterns = [

            r"amounts?\s+in\s+(thousands|millions|billions|trillions)",

            r"figures?\s+in\s+(thousands|millions|billions|trillions)",

            r"reported\s+in\s+(thousands|millions|billions|trillions)",

            r"expressed\s+in\s+(thousands|millions|billions|trillions)",

            r"usd\s+in\s+(thousands|millions|billions|trillions)",

            r"all\s+amounts?\s+.*?(thousands|millions|billions|trillions)",

            r"\((thousands|millions|billions|trillions)\)",

        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                header,
                flags=re.IGNORECASE,
            )

            if match:

                unit = match.group(1).lower()

                return {

                    "unit": unit,

                    "multiplier":
                        self.UNIT_MULTIPLIERS.get(
                            unit,
                            1,
                        ),

                }

        return {

            "unit": None,

            "multiplier": 1,

        }

    def normalize(self, value, multiplier):
        """
        Normalize a financial value.

        Example:

        391035 + million

        →

        391035000000
        """

        if value is None:
            return None

        try:

            return int(float(value) * multiplier)

        except Exception:

            return value