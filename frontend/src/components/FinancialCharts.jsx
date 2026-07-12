import { useMemo } from "react";

import "../styles/FinancialCharts.css";

import MetricBarChart from "./MetricBarChart";
import KPICards from "./KPICards";
import FinancialHealthScore from "./FinancialHealthScore";
import FinancialInsights from "./FinancialInsights";

import { parseMetricValue } from "../utils/metricUtils";

function FinancialCharts({ comparisonData }) {

    const metrics = [
        { key: "revenue", label: "Revenue" },
        { key: "net_income", label: "Net Income" },
        { key: "gross_profit", label: "Gross Profit" },
        { key: "operating_income", label: "Operating Income" },
        { key: "eps", label: "EPS" },
        { key: "cash", label: "Cash" },
    ];

    const chartData = useMemo(() => {

        if (
            !comparisonData ||
            !comparisonData.documents
        ) {
            return {};
        }

        const data = {};

        metrics.forEach((metric) => {

            data[metric.key] = comparisonData.documents.map((document) => ({

                name: document.name.replace(".pdf", ""),

                [metric.key]:
                    parseMetricValue(
                        document.metrics?.[metric.key]
                    ) || 0,

            }));

        });

        return data;

    }, [comparisonData]);

    if (
        !comparisonData ||
        !comparisonData.documents ||
        comparisonData.documents.length === 0
    ) {
        return null;
    }

    return (

        <div className="financial-charts">

            <h2 className="financial-charts-title">
                📈 Financial Analytics
            </h2>

            <KPICards
                comparisonData={comparisonData}
            />

            <FinancialHealthScore
                comparisonData={comparisonData}
            />
            
            <FinancialInsights
                insights={comparisonData.insights}
            />


            <div className="charts-grid"></div>

            <div className="charts-grid">

                {metrics.map((metric) => (

                    <MetricBarChart
                        key={metric.key}
                        title={metric.label}
                        data={chartData[metric.key]}
                        dataKey={metric.key}
                    />

                ))}

            </div>

        </div>

    );

}

export default FinancialCharts;