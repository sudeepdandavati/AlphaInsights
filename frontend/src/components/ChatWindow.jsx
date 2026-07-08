import { useEffect, useRef } from "react";

import Welcome from "./Welcome";
import Message from "./Message";
import SourceList from "./SourceList";

function ChatWindow({ messages, onSuggestionClick }) {
    // Reference to the bottom of the chat
    const bottomRef = useRef(null);

    // Auto-scroll whenever a new message is added
    useEffect(() => {
        bottomRef.current?.scrollIntoView({
            behavior: "smooth",
        });
    }, [messages]);

    // Show welcome screen when there are no conversations
    if (messages.length === 0) {
        return (
            <div className="chat-window">
                <Welcome onSuggestionClick={onSuggestionClick} />
            </div>
        );
    }

    return (
        <div className="chat-window">
            {messages.map((message, index) => (
                <div
                    key={index}
                    className="conversation-card"
                >
                    <div className="user-card">
                        <h3>👤 You</h3>
                        <p>{message.question}</p>
                    </div>

                    <div className="assistant-card">
                        <h3>🤖 AlphaInsights</h3>

                        <Message
                            response={{
                                answer: message.answer,
                            }}
                        />

                        <SourceList
                            sources={message.sources}
                        />
                    </div>
                </div>
            ))}

            {/* Invisible element used for auto-scroll */}
            <div ref={bottomRef}></div>
        </div>
    );
}

export default ChatWindow;