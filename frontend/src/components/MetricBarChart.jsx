import {
    ResponsiveContainer,
    BarChart,
    Bar,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    Cell,
} from "recharts";

function formatValue(value) {

    if (value >= 1e12) {
        return `${(value / 1e12).toFixed(2)}T`;
    }

    if (value >= 1e9) {
        return `${(value / 1e9).toFixed(2)}B`;
    }

    if (value >= 1e6) {
        return `${(value / 1e6).toFixed(2)}M`;
    }

    if (value >= 1e3) {
        return `${(value / 1e3).toFixed(2)}K`;
    }

    return value;

}

function MetricBarChart({
    title,
    data,
    dataKey,
}) {

    const sortedData = [...data].sort(
        (a, b) => b[dataKey] - a[dataKey]
    );

    return (

        <div className="metric-chart">

            <h3 className="metric-chart-title">
                {title}
            </h3>

            <ResponsiveContainer
                width="100%"
                height={380}
            >

                <BarChart
                    data={sortedData}
                    margin={{
                        top: 20,
                        right: 30,
                        left: 20,
                        bottom: 10,
                    }}
                >

                    <CartesianGrid strokeDasharray="3 3" />

                    <XAxis
                        dataKey="name"
                    />

                    <YAxis
                        tickFormatter={formatValue}
                    />

                    <Tooltip
                        formatter={(value) => formatValue(value)}
                    />

                    <Bar
                        dataKey={dataKey}
                        radius={[8, 8, 0, 0]}
                        animationDuration={1200}
                        animationEasing="ease-out"
                    >

                        {sortedData.map((entry, index) => (

                            <Cell
                                key={index}
                                fill={
                                    index === 0
                                        ? "#22c55e"
                                        : "#3b82f6"
                                }
                            />

                        ))}

                    </Bar>

                </BarChart>

            </ResponsiveContainer>

        </div>

    );

}

export default MetricBarChart;