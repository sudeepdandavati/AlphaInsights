import re


class RowParser:
    """
    Converts cleaned document lines into logical financial rows.

    Examples:

    Revenue
    391,035

        ↓

    Revenue 391,035


    Revenue
    $
    391,035

        ↓

    Revenue 391,035


    Revenue .......... 391,035

        ↓

    Revenue 391,035
    """

    def parse(self, lines):
        """
        Merge related lines into logical rows.

        Args:
            lines (list[str])

        Returns:
            list[str]
        """

        rows = []

        i = 0

        while i < len(lines):

            current = lines[i].strip()

            if not current:
                i += 1
                continue

            # Skip standalone currency symbols
            if current in {"$", "€", "£"}:
                i += 1
                continue

            row = current

            j = i + 1

            while j < len(lines):

                candidate = lines[j].strip()

                if not candidate:
                    j += 1
                    continue

                # Currency symbol
                if candidate in {"$", "€", "£"}:
                    j += 1
                    continue

                # Financial number
                if re.fullmatch(
                    r"[\d,]+(?:\.\d+)?\s?[KMBT]?",
                    candidate,
                    flags=re.IGNORECASE,
                ):

                    row += " " + candidate

                    j += 1

                    break

                # Stop if another heading starts
                if re.match(
                    r"[A-Za-z]",
                    candidate,
                ):
                    break

                j += 1

            rows.append(row)

            i = j

        return rows