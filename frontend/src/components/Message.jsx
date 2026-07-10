import { useState } from "react";

import "../styles/Message.css";

function Message({ response, loading }) {

    const [copied, setCopied] = useState(false);

    // ----------------------------------------
    // Copy Answer
    // ----------------------------------------

    const handleCopy = async () => {

        if (!response?.answer) return;

        try {

            await navigator.clipboard.writeText(response.answer);

            setCopied(true);

            setTimeout(() => {

                setCopied(false);

            }, 2000);

        } catch (error) {

            console.error("Failed to copy:", error);

        }

    };

    // ----------------------------------------
    // Typing Indicator
    // ----------------------------------------

    if (loading) {

        return (

            <div className="message typing-message">

                <div className="typing-indicator">

                    <span></span>
                    <span></span>
                    <span></span>

                </div>

            </div>

        );

    }

    if (!response) return null;

    return (

        <div className="message">

            <p className="message-text">
                {response.answer}
            </p>

            <div className="message-actions">

                <button
                    className="copy-button"
                    onClick={handleCopy}
                >

                    {copied ? "✅ Copied" : "📋 Copy"}

                </button>

            </div>

        </div>

    );

}

export default Message;