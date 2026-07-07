import { useState } from "react";
import { askQuestion } from "../services/api";

function ChatBox({ onResponse }) {
    const [question, setQuestion] = useState("");
    const [loading, setLoading] = useState(false);

    const handleSubmit = async () => {
        if (!question.trim()) return;

        setLoading(true);

        try {
            const result = await askQuestion(question);

            onResponse(result);

            setQuestion("");
        } catch (error) {
            alert("Failed to contact the backend.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="chat-box">
            <textarea
                rows="4"
                placeholder="Ask a question about the financial report..."
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
            />

            <button
                onClick={handleSubmit}
                disabled={loading}
            >
                {loading ? "Thinking..." : "Ask AI"}
            </button>
        </div>
    );
}

export default ChatBox;