import re

from extraction.metric_dictionary import METRIC_DICTIONARY
from extraction.metric_rules import MetricRules
from extraction.validator import MetricValidator
from extraction.line_parser import LineParser
from extraction.row_parser import RowParser


class FinancialMetricsExtractor:
    """
    Production-ready Financial Metrics Extraction Engine.

    Pipeline

    Raw Text
        ↓
    Line Parser
        ↓
    Row Parser
        ↓
    Candidate Extraction
        ↓
    Metric Rules
        ↓
    Validation
        ↓
    Unit Normalization
        ↓
    Final Metrics
    """

    NUMBER_REGEX = re.compile(
        r"\b\d[\d,]*(?:\.\d+)?(?:\s*[KMBT])?\b",
        flags=re.IGNORECASE,
    )

    def __init__(self):

        self.metric_dictionary = METRIC_DICTIONARY

        self.line_parser = LineParser()

        self.row_parser = RowParser()

    # --------------------------------------------------
    # Public API
    # --------------------------------------------------

    def extract(
        self,
        text,
        multiplier=1,
    ):
        """
        Extract every supported financial metric.

        Parameters
        ----------
        text : str
            Cleaned document text.

        multiplier : int
            Reporting-unit multiplier
            (1, 1000, 1000000, ...)

        Returns
        -------
        dict
        """

        rows = self._prepare_rows(text)

        metrics = {}

        for metric_name, aliases in self.metric_dictionary.items():

            candidate = self._find_metric(
                rows,
                metric_name,
                aliases,
            )

            metrics[metric_name] = self._build_metric(
                metric_name=metric_name,
                candidate=candidate,
                multiplier=multiplier,
            )

        return metrics

    # --------------------------------------------------
    # Internal Pipeline
    # --------------------------------------------------

    def _prepare_rows(self, text):
        """
        Convert cleaned text into logical financial rows.

        Returns
        -------
        list[str]
        """

        if not text:
            return []

        lines = self.line_parser.parse(text)

        rows = self.row_parser.parse(lines)

        return rows

    # --------------------------------------------------
    # Candidate Search
    # --------------------------------------------------

    def _find_metric(
        self,
        rows,
        metric_name,
        aliases,
    ):
        """
        Find the best matching metric from all rows.
        """

        all_candidates = []

        # Enable this while debugging
        DEBUG = True

        if DEBUG:
            print(f"\n========== Searching: {metric_name} ==========")

        for row in rows:
            normalized_row = " ".join(row.split()).lower()
            matched_alias = None
            
            for alias in aliases:
                alias_lower = alias.lower()
                
                if normalized_row.startswith(alias_lower):
                    matched_alias = alias
                    break
            
            if matched_alias is None:
                
                for alias in aliases:
                    
                    alias_lower = alias.lower()
                    
                    if alias_lower in normalized_row:
                        matched_alias = alias
                        break
            if matched_alias is None:
                continue
            
            if DEBUG:
                print(f"Matched Alias : {matched_alias}")
                print(f"Row           : {row}")


            candidates = self._extract_candidates(
                row,
                metric_name,
            )

            if matched_alias is not None:
                for candidate in candidates:
                    
                    if normalized_row.startswith(matched_alias.lower()):
                        candidate["score"] += 1_000_000

            if DEBUG and candidates:
                print("Candidates:")

                for candidate in candidates:
                    print(
                        f"  {candidate['raw']} "
                        f"(score={candidate['score']})"
                    )

            all_candidates.extend(candidates)

        best = self._select_best_candidate(
            all_candidates,
        )

        if DEBUG:
            print(f"Best Candidate: {best}")

        return best


    def _extract_candidates(
        self,
        row,
        metric_name,
    ):
        """
        Extract every possible numeric candidate from a row.

        Returns
        -------
        list[dict]
        """

        if not row:
            return []

        matches = self.NUMBER_REGEX.findall(row)

        if not matches:
            return []

        multipliers = {
            "": 1,
            "K": 1_000,
            "M": 1_000_000,
            "B": 1_000_000_000,
            "T": 1_000_000_000_000,
        }

        candidates = []

        for raw_value in matches:

            cleaned = raw_value.replace(",", "").strip()

            suffix = ""

            if cleaned and cleaned[-1].upper() in multipliers:
                suffix = cleaned[-1].upper()
                cleaned = cleaned[:-1].strip()

            try:
                numeric = float(cleaned)

            except ValueError:
                continue

            numeric_value = numeric * multipliers[suffix]
            # Ignore years such as 2022, 2023, 2024
            if (
                suffix == ""
                and metric_name != "eps"
                and 1900 <= numeric_value <= 2100
                ):
                continue

            # Ignore likely note/reference numbers
            if numeric_value < 100 and metric_name != "eps":
                continue

            score = MetricRules.score(
                metric_name,
                numeric_value,
            )

            # Ignore invalid candidates
            if score < 0:
                continue

            candidates.append(
                {
                    "raw": raw_value,
                    "numeric": numeric_value,
                    "score": score,
                    "row": row,
                }
            )

        return candidates


    def _select_best_candidate(
        self,
        candidates,
    ):
        """
        Select the highest-scoring candidate.
        """

        if not candidates:
            return None

        return max(
            candidates,
            key=lambda candidate: candidate["score"],
        )
    # --------------------------------------------------
    # Metric Builder
    # --------------------------------------------------

    def _build_metric(
        self,
        metric_name,
        candidate,
        multiplier,
    ):
        """
        Validate and normalize a metric.

        Parameters
        ----------
        metric_name : str

        candidate : dict | None

        multiplier : int

        Returns
        -------
        int | float | None
        """

        if candidate is None:
            return None

        validated = MetricValidator.validate(
            metric_name,
            candidate["raw"],
        )

        if validated is None:
            return None

        try:
            return validated * multiplier
        except TypeError:
            return validated