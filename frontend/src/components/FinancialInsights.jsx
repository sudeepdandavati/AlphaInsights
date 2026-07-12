import "../styles/FinancialInsights.css";

function FinancialInsights({ insights }) {

    if (!insights) {
        return null;
    }

    return (

        <div className="financial-insights">

            <h2 className="financial-insights-title">
                🤖 AI Financial Insights
            </h2>

            <div className="financial-insights-card">

                <p className="financial-insights-text">
                    {insights}
                </p>

            </div>

        </div>

    );

}

export default FinancialInsights;