import re


class LineParser:
    """
    Utility class for normalizing and cleaning
    lines extracted from financial reports.

    Responsibilities:

    - Split text into lines
    - Remove empty lines
    - Normalize whitespace
    - Remove obvious page numbers
    - Remove repeated separators
    """

    def parse(self, text):
        """
        Convert raw document text into clean lines.

        Args:
            text (str)

        Returns:
            list[str]
        """

        if not text:
            return []

        raw_lines = text.splitlines()

        cleaned_lines = []

        for line in raw_lines:

            line = self.clean_line(line)

            if line:
                cleaned_lines.append(line)

        return cleaned_lines

    def clean_line(self, line):
        """
        Clean a single line.
        """

        if line is None:
            return None

        line = line.strip()

        if not line:
            return None

        # Collapse multiple spaces
        line = re.sub(
            r"\s+",
            " ",
            line,
        )

        # Remove dotted leaders
        # Revenue ........ 391,035
        line = re.sub(
            r"\.{2,}",
            " ",
            line,
        )

        # Remove long separator lines
        line = re.sub(
            r"[-_=]{4,}",
            "",
            line,
        )

        line = line.strip()

        if not line:
            return None

        # Ignore page numbers
        if re.fullmatch(r"\d{1,4}", line):
            return None

        # Ignore "Page X"
        if re.fullmatch(
            r"Page\s+\d+",
            line,
            flags=re.IGNORECASE,
        ):
            return None

        return line

    def next_non_empty_line(
        self,
        lines,
        index,
        max_distance=3,
    ):
        """
        Return the next meaningful line.

        Example

        Revenue

        391,035

        Returns "391,035"
        """

        for offset in range(1, max_distance + 1):

            next_index = index + offset

            if next_index >= len(lines):
                break

            candidate = lines[next_index].strip()

            if candidate:
                return candidate

        return None

    def previous_non_empty_line(
        self,
        lines,
        index,
        max_distance=3,
    ):
        """
        Return previous meaningful line.
        """

        for offset in range(1, max_distance + 1):

            previous_index = index - offset

            if previous_index < 0:
                break

            candidate = lines[previous_index].strip()

            if candidate:
                return candidate

        return None

    def is_numeric_line(self, line):
        """
        Check whether a line primarily contains
        a financial number.
        """

        if not line:
            return False

        return bool(

            re.fullmatch(

                r"[$€£]?\s*[\d,]+(?:\.\d+)?\s?[KMBT]?",

                line.strip(),

            )

        )