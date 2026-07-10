import { useEffect, useState } from "react";

import "./App.css";

import Header from "./components/Header";
import UploadBox from "./components/UploadBox";
import DocumentInfo from "./components/DocumentInfo";
import ExportChat from "./components/ExportChat";
import ChatWindow from "./components/ChatWindow";
import ChatBox from "./components/ChatBox";
import Notification from "./components/Notification";

import {
    askQuestion,
    uploadPDF,
} from "./services/api";

const CHAT_STORAGE_KEY = "alphainsights-chat";
const DOCUMENT_STORAGE_KEY = "alphainsights-document";

function App() {

    // ----------------------------------------
    // Global State
    // ----------------------------------------

    const [messages, setMessages] = useState([]);
    const [question, setQuestion] = useState("");

    const [loading, setLoading] = useState(false);
    const [uploading, setUploading] = useState(false);

    const [documentInfo, setDocumentInfo] = useState(null);

    const [notification, setNotification] = useState({
        type: "",
        message: "",
    });

    // ----------------------------------------
    // Restore saved session
    // ----------------------------------------

    useEffect(() => {

        const savedMessages = localStorage.getItem(CHAT_STORAGE_KEY);
        const savedDocument = localStorage.getItem(DOCUMENT_STORAGE_KEY);

        if (savedMessages) {
            setMessages(JSON.parse(savedMessages));
        }

        if (savedDocument) {
            setDocumentInfo(JSON.parse(savedDocument));
        }

    }, []);

    // ----------------------------------------
    // Save chat whenever it changes
    // ----------------------------------------

    useEffect(() => {

        localStorage.setItem(
            CHAT_STORAGE_KEY,
            JSON.stringify(messages)
        );

    }, [messages]);

    // ----------------------------------------
    // Save document whenever it changes
    // ----------------------------------------

    useEffect(() => {

        if (documentInfo) {

            localStorage.setItem(
                DOCUMENT_STORAGE_KEY,
                JSON.stringify(documentInfo)
            );

        }

    }, [documentInfo]);

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

            setQuestion("");

            localStorage.removeItem(CHAT_STORAGE_KEY);

            localStorage.setItem(
                DOCUMENT_STORAGE_KEY,
                JSON.stringify(result)
            );

            setNotification({
                type: "success",
                message: "Document uploaded and indexed successfully.",
            });

        } catch (error) {

            setNotification({
                type: "error",
                message: "Failed to upload the document.",
            });

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

            setNotification({
                type: "warning",
                message: "Please upload a financial report first.",
            });

            return;

        }

        setLoading(true);

        setQuestion("");

        // Show temporary AI typing message

        setMessages((prev) => [

            ...prev,

            {

                question: query,

                answer: "",

                sources: [],

                isLoading: true,

            },

        ]);

        try {

            const response = await askQuestion(query);

            setMessages((prev) => {

                const updated = [...prev];

                updated[updated.length - 1] = {

                    question: query,

                    answer: response.answer,

                    sources: response.sources,

                    isLoading: false,

                };

                return updated;

            });

        } catch (error) {

            setMessages((prev) => {

                const updated = [...prev];

                updated[updated.length - 1] = {

                    question: query,

                    answer: "Unable to generate a response.",

                    sources: [],

                    isLoading: false,

                };

                return updated;

            });

            setNotification({

                type: "error",

                message: "Failed to contact the backend.",

            });

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

            <Notification
                type={notification.type}
                message={notification.message}
                onClose={() =>
                    setNotification({
                        type: "",
                        message: "",
                    })
                }
            />

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

            <ExportChat
                messages={messages}
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