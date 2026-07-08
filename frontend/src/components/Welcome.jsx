function Welcome({ onSuggestionClick }) {

    const suggestions = [
        {
            icon: "📈",
            title: "Revenue in 2024",
            question: "What was Apple's revenue in 2024?"
        },
        {
            icon: "📱",
            title: "iPad Sales",
            question: "Why did iPad sales decrease?"
        },
        {
            icon: "📊",
            title: "Gross Margin",
            question: "What was Apple's gross margin?"
        },
        {
            icon: "💰",
            title: "Share Repurchases",
            question: "How much cash did Apple spend on share repurchases?"
        }
    ];

    return (
        <div className="welcome">

            <div className="welcome-icon">
                🤖
            </div>

            <h2>Welcome to AlphaInsights</h2>

            <p>
                Ask questions about annual reports,
                financial statements and SEC filings.
            </p>

            <div className="suggestion-grid">

                {suggestions.map((item, index) => (

                    <div
                        key={index}
                        className="suggestion-card"
                        onClick={() => onSuggestionClick(item.question)}
                    >
                        <div className="suggestion-icon">
                            {item.icon}
                        </div>

                        <h3>{item.title}</h3>

                        <p>{item.question}</p>

                    </div>

                ))}

            </div>

        </div>
    );
}

export default Welcome;