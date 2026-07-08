import "../styles/ChatBox.css";

function ChatBox({
    question,
    setQuestion,
    loading,
    onSubmit,
}) {
    const handleKeyDown = (event) => {
        if (event.key === "Enter" && !event.shiftKey) {
            event.preventDefault();
            onSubmit();
        }
    };

    return (
        <div className="chat-box">

            <div className="chat-input-container">

                <textarea
                    className="chat-input"
                    rows="1"
                    placeholder="Ask anything about your financial report..."
                    value={question}
                    disabled={loading}
                    onChange={(e) => setQuestion(e.target.value)}
                    onKeyDown={handleKeyDown}
                />

                <button
                    className="send-button"
                    onClick={onSubmit}
                    disabled={loading || !question.trim()}
                >
                    {loading ? "..." : "➜"}
                </button>

            </div>

        </div>
    );
}

export default ChatBox;