import { useEffect, useRef } from "react";

import "../styles/ChatBox.css";

function ChatBox({
    question,
    setQuestion,
    loading,
    onSubmit,
}) {

    const textareaRef = useRef(null);

    // ----------------------------------------
    // Auto-grow textarea
    // ----------------------------------------

    useEffect(() => {

        if (!textareaRef.current) return;

        textareaRef.current.style.height = "auto";

        textareaRef.current.style.height =
            `${textareaRef.current.scrollHeight}px`;

    }, [question]);

    // ----------------------------------------
    // Focus after loading completes
    // ----------------------------------------

    useEffect(() => {

        if (!loading && textareaRef.current) {

            textareaRef.current.focus();

            textareaRef.current.style.height = "auto";

        }

    }, [loading]);

    // ----------------------------------------
    // Keyboard shortcuts
    // ----------------------------------------

    const handleKeyDown = (event) => {

        // Shift + Enter = new line
        if (event.key === "Enter" && event.shiftKey) {
            return;
        }

        // Enter = Send
        if (event.key === "Enter") {

            event.preventDefault();

            if (!loading && question.trim()) {
                onSubmit();
            }

        }

    };

    return (

        <div className="chat-box">

            <div className="chat-input-container">

                <textarea
                    ref={textareaRef}
                    className="chat-input"
                    rows={1}
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

                    {loading ? (

                        <span className="button-spinner"></span>

                    ) : (

                        "➜"

                    )}

                </button>

            </div>

        </div>

    );

}

export default ChatBox;