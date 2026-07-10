import { useState } from "react";

import "./App.css";

import Header from "./components/Header";
import UploadBox from "./components/UploadBox";
import DocumentInfo from "./components/DocumentInfo";
import ChatWindow from "./components/ChatWindow";
import ChatBox from "./components/ChatBox";

import {
    askQuestion,
    uploadPDF,
} from "./services/api";

function App() {

    // ----------------------------------------
    // Global State
    // ----------------------------------------

    const [messages, setMessages] = useState([]);
    const [question, setQuestion] = useState("");

    const [loading, setLoading] = useState(false);
    const [uploading, setUploading] = useState(false);

    const [documentInfo, setDocumentInfo] = useState(null);

    // ----------------------------------------
    // Upload PDF
    // ----------------------------------------

    const handleUpload = async (file) => {

        setUploading(true);

        try {

            const result = await uploadPDF(file);

            setDocumentInfo(result);

            // Clear previous conversation
            setMessages([]);

            // Clear input
            setQuestion("");

        } catch (error) {

            alert("Failed to upload document.");

        } finally {

            setUploading(false);

        }

    };

    // ----------------------------------------
    // Submit Question
    // ----------------------------------------

    const handleSubmit = async (query = question) => {

        if (!query.trim()) return;

        if (!documentInfo) {

            alert("Please upload a financial report first.");

            return;

        }

        setLoading(true);

        try {

            const response = await askQuestion(query);

            setMessages((prevMessages) => [
                ...prevMessages,
                {
                    question: query,
                    answer: response.answer,
                    sources: response.sources,
                },
            ]);

            setQuestion("");

        } catch (error) {

            alert("Failed to contact the backend.");

        } finally {

            setLoading(false);

        }

    };

    // ----------------------------------------
    // Suggestion Cards
    // ----------------------------------------

    const handleSuggestionClick = async (suggestion) => {

        setQuestion(suggestion);

        await handleSubmit(suggestion);

    };

    return (

        <div className="app">

            <Header />

            <UploadBox
                onUpload={handleUpload}
            />

            {uploading && (
                <p
                    style={{
                        textAlign: "center",
                        color: "#94a3b8",
                        marginTop: "12px",
                    }}
                >
                    ⏳ Processing document...
                </p>
            )}

            <DocumentInfo
                documentInfo={documentInfo}
            />

            <ChatWindow
                messages={messages}
                documentInfo={documentInfo}
                onSuggestionClick={handleSuggestionClick}
            />

            <ChatBox
                question={question}
                setQuestion={setQuestion}
                loading={loading}
                onSubmit={handleSubmit}
            />

        </div>

    );
}

export default App;