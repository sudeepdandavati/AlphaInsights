import "../styles/FinancialHealthScore.css";

import { calculateFinancialHealth } from "../utils/financialHealth";

function FinancialHealthScore({ comparisonData }) {

    if (
        !comparisonData ||
        !comparisonData.documents ||
        comparisonData.documents.length === 0
    ) {
        return null;
    }

    const scores = calculateFinancialHealth(
        comparisonData.documents
    );

    const getScoreClass = (score) => {

        if (score >= 85) {
            return "score-excellent";
        }

        if (score >= 70) {
            return "score-good";
        }

        if (score >= 50) {
            return "score-average";
        }

        return "score-poor";

    };

    return (

        <div className="financial-health">

            <h2 className="financial-health-title">
                🏥 Financial Health Scores
            </h2>

            <div className="health-grid">

                {scores.map((company, index) => (

                    <div
                        key={company.id}
                        className={`health-card ${getScoreClass(company.score)}`}
                    >

                        <div className="health-rank">

                            {index === 0 && "🥇"}

                            {index === 1 && "🥈"}

                            {index === 2 && "🥉"}

                            {index > 2 && `#${index + 1}`}

                        </div>

                        <div className="health-company">
                            {company.company}
                        </div>

                        <div className="health-score">
                            {company.score}/100
                        </div>

                    </div>

                ))}

            </div>

        </div>

    );

}

export default FinancialHealthScore;