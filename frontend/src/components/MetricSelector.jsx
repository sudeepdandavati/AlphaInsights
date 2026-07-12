function MetricSelector({
    selectedMetric,
    onMetricChange,
}) {

    const metrics = [
        {
            value: "revenue",
            label: "Revenue",
        },
        {
            value: "net_income",
            label: "Net Income",
        },
        {
            value: "gross_profit",
            label: "Gross Profit",
        },
        {
            value: "operating_income",
            label: "Operating Income",
        },
        {
            value: "eps",
            label: "EPS",
        },
        {
            value: "cash",
            label: "Cash",
        },
        {
            value: "total_assets",
            label: "Total Assets",
        },
        {
            value: "total_liabilities",
            label: "Total Liabilities",
        },
        {
            value: "total_debt",
            label: "Total Debt",
        },
    ];

    return (

        <div className="metric-selector">

            <label className="metric-selector-label">
                Select Metric
            </label>

            <select
                className="metric-selector-dropdown"
                value={selectedMetric}
                onChange={(event) =>
                    onMetricChange(event.target.value)
                }
            >

                {metrics.map((metric) => (

                    <option
                        key={metric.value}
                        value={metric.value}
                    >
                        {metric.label}
                    </option>

                ))}

            </select>

        </div>

    );

}

export default MetricSelector;