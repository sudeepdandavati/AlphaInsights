import "../styles/Comparison.css";

import {
    getHighestValue,
    getLowestValue,
    getMetricClass,
} from "../utils/metricUtils";

function ComparisonTable({ comparisonData }) {

    if (
        !comparisonData ||
        !comparisonData.documents ||
        comparisonData.documents.length === 0
    ) {
        return null;
    }

    const metrics = [
        { key: "revenue", label: "Revenue" },
        { key: "net_income", label: "Net Income" },
        { key: "gross_profit", label: "Gross Profit" },
        { key: "operating_income", label: "Operating Income" },
        { key: "eps", label: "EPS" },
        { key: "cash", label: "Cash" },
        { key: "total_assets", label: "Total Assets" },
        { key: "total_liabilities", label: "Total Liabilities" },
        { key: "total_debt", label: "Total Debt" },
    ];

    return (

        <div className="comparison-table-container">

            <h2 className="comparison-title">
                📊 Financial Comparison
            </h2>

            <table className="comparison-table">

                <thead>

                    <tr>

                        <th>Metric</th>

                        {comparisonData.documents.map((document) => (

                            <th key={document.id}>
                                {document.name}
                            </th>

                        ))}

                    </tr>

                </thead>

                <tbody>

                    {metrics.map((metric) => {

                        const values = comparisonData.documents.map(
                            (document) => document.metrics?.[metric.key]
                        );

                        const highest = getHighestValue(values);

                        const lowest = getLowestValue(values);

                        return (

                            <tr key={metric.key}>

                                <td className="metric-name">
                                    {metric.label}
                                </td>

                                {comparisonData.documents.map((document) => {

                                    const value =
                                        document.metrics?.[metric.key] || "—";

                                    return (

                                        <td
                                            key={document.id}
                                            className={getMetricClass(
                                                value,
                                                highest,
                                                lowest
                                            )}
                                        >
                                            {value}
                                        </td>

                                    );

                                })}

                            </tr>

                        );

                    })}

                </tbody>

            </table>

        </div>

    );

}

export default ComparisonTable;