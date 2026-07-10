import { useEffect, useRef } from "react";

import "../styles/ChatWindow.css";

import Welcome from "./Welcome";
import Message from "./Message";
import SourceList from "./SourceList";

function ChatWindow({
    messages,
    onSuggestionClick,
    documentInfo,
}) {

    const bottomRef = useRef(null);

    useEffect(() => {
        bottomRef.current?.scrollIntoView({
            behavior: "smooth",
        });
    }, [messages]);

    // ----------------------------------------
    // No document uploaded
    // ----------------------------------------

    if (!documentInfo) {
        return (
            <div className="chat-window">
                <Welcome
                    onSuggestionClick={onSuggestionClick}
                />
            </div>
        );
    }

    // ----------------------------------------
    // Document uploaded but no questions yet
    // ----------------------------------------

    if (messages.length === 0) {
        return (
            <div className="chat-window">

                <div className="empty-chat">

                    <div className="empty-chat-icon">
                        💬
                    </div>

                    <h2>
                        Ask your first question
                    </h2>

                    <p>
                        Your document
                        <strong> {documentInfo.document.name}</strong>
                        {" "}has been indexed successfully.
                    </p>

                    <p>
                        Start asking questions about the report.
                    </p>

                </div>

            </div>
        );
    }

    // ----------------------------------------
    // Conversation
    // ----------------------------------------

    return (

        <div className="chat-window">

            {messages.map((message, index) => (

                <div
                    key={index}
                    className="conversation-card"
                >

                    {/* ---------------- User ---------------- */}

                    <div className="user-card">

                        <h3>👤 You</h3>

                        <p>{message.question}</p>

                    </div>

                    {/* ---------------- Assistant ---------------- */}

                    <div className="assistant-card">

                        <h3>🤖 AlphaInsights</h3>

                        <Message
                            response={{
                                answer: message.answer,
                            }}
                            loading={message.isLoading}
                        />

                        {!message.isLoading && (
                            <SourceList
                                sources={message.sources}
                            />
                        )}

                    </div>

                </div>

            ))}

            <div ref={bottomRef} />

        </div>

    );
}

export default ChatWindow;