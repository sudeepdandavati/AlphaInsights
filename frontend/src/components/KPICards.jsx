import "../styles/KPICards.css";

import { parseMetricValue } from "../utils/metricUtils";

function KPICards({ comparisonData }) {

    if (
        !comparisonData ||
        !comparisonData.documents ||
        comparisonData.documents.length === 0
    ) {
        return null;
    }

    const getHighest = (metric) => {

        let best = null;

        comparisonData.documents.forEach((document) => {

            const value = parseMetricValue(
                document.metrics?.[metric]
            );

            if (value === null) {
                return;
            }

            if (!best || value > best.value) {

                best = {
                    company: document.name.replace(".pdf", ""),
                    value,
                    display: document.metrics?.[metric],
                };

            }

        });

        return best;

    };

    const getLowest = (metric) => {

        let best = null;

        comparisonData.documents.forEach((document) => {

            const value = parseMetricValue(
                document.metrics?.[metric]
            );

            if (value === null) {
                return;
            }

            if (!best || value < best.value) {

                best = {
                    company: document.name.replace(".pdf", ""),
                    value,
                    display: document.metrics?.[metric],
                };

            }

        });

        return best;

    };

    const revenue = getHighest("revenue");
    const cash = getHighest("cash");
    const eps = getHighest("eps");
    const debt = getLowest("total_debt");

    const cards = [
        {
            icon: "🏆",
            title: "Highest Revenue",
            data: revenue,
        },
        {
            icon: "💰",
            title: "Highest Cash",
            data: cash,
        },
        {
            icon: "📈",
            title: "Highest EPS",
            data: eps,
        },
        {
            icon: "📉",
            title: "Lowest Debt",
            data: debt,
        },
    ];

    return (

        <div className="kpi-grid">

            {cards.map((card) => (

                <div
                    key={card.title}
                    className="kpi-card"
                >

                    <div className="kpi-icon">
                        {card.icon}
                    </div>

                    <div className="kpi-title">
                        {card.title}
                    </div>

                    <div className="kpi-company">
                        {card.data
                            ? card.data.company
                            : "—"}
                    </div>

                    <div className="kpi-value">
                        {card.data
                            ? card.data.display
                            : "—"}
                    </div>

                </div>

            ))}

        </div>

    );

}

export default KPICards;