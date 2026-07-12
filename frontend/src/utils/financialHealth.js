import { parseMetricValue } from "./metricUtils";

/*
----------------------------------------
Financial Health Scoring
----------------------------------------

Weights

Revenue           30
Net Income        30
Cash              20
Debt              20

Total            100
*/

const METRIC_WEIGHTS = {
    revenue: 30,
    net_income: 30,
    cash: 20,
    total_debt: 20,
};

// ----------------------------------------
// Rank documents for one metric
// ----------------------------------------

function rankDocuments(documents, metric, descending = true) {

    const ranked = [...documents].sort((a, b) => {

        const valueA = parseMetricValue(
            a.metrics?.[metric]
        ) ?? 0;

        const valueB = parseMetricValue(
            b.metrics?.[metric]
        ) ?? 0;

        return descending
            ? valueB - valueA
            : valueA - valueB;

    });

    return ranked;

}

// ----------------------------------------
// Calculate Financial Health Scores
// ----------------------------------------

export function calculateFinancialHealth(documents) {

    const scores = {};

    documents.forEach((document) => {

        scores[document.id] = {
            id: document.id,
            company: document.name.replace(".pdf", ""),
            score: 0,
        };

    });

    Object.entries(METRIC_WEIGHTS).forEach(
        ([metric, weight]) => {

            const descending =
                metric !== "total_debt";

            const ranked = rankDocuments(
                documents,
                metric,
                descending
            );

            const maxRank = ranked.length - 1;

            ranked.forEach((document, index) => {

                const points =
                    maxRank === 0
                        ? weight
                        : weight *
                          ((maxRank - index) / maxRank);

                scores[document.id].score += points;

            });

        }
    );

    return Object.values(scores)

        .map((company) => ({
            ...company,
            score: Math.round(company.score),
        }))

        .sort((a, b) => b.score - a.score);

}