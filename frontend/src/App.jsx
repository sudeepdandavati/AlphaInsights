import { useEffect, useState } from "react";
import "./App.css";

import Header from "./components/Header";
import UploadBox from "./components/UploadBox";
import DocumentSidebar from "./components/DocumentSidebar";
import DocumentInfo from "./components/DocumentInfo";
import ExportChat from "./components/ExportChat";
import ChatWindow from "./components/ChatWindow";
import ChatBox from "./components/ChatBox";
import Notification from "./components/Notification";
import FinancialDashboard from "./components/FinancialDashboard";
import ComparisonWorkspace from "./components/ComparisonWorkspace";

import {
    askQuestion,
    uploadPDF,
    getDocuments,
} from "./services/api";

const CHAT_STORAGE_KEY = "alphainsights-chat";
const DOCUMENT_STORAGE_KEY = "alphainsights-document";

function App() {
    //----------------------------------------
    // Global State
    //----------------------------------------

    const [messages, setMessages] = useState([]);
    const [question, setQuestion] = useState("");

    const [loading, setLoading] = useState(false);
    const [uploading, setUploading] = useState(false);

    const [documentInfo, setDocumentInfo] = useState(null);

    //----------------------------------------
    // Multi-document State
    //----------------------------------------

    const [documents, setDocuments] = useState([]);
    const [selectedDocument, setSelectedDocument] = useState(null);

    const [notification, setNotification] = useState({
        type: "",
        message: "",
    });

    //----------------------------------------
    // Notification Helper
    //----------------------------------------

    const showNotification = (type, message) => {
        setNotification({ type, message });

        setTimeout(() => {
            setNotification({
                type: "",
                message: "",
            });
        }, 3000);
    };

    //----------------------------------------
// Load Documents
//----------------------------------------

const loadDocuments = async () => {
    try {

        const docs = await getDocuments();

        setDocuments(docs);

        if (docs.length === 0) return;

        setSelectedDocument((current) => {

            if (!current) {
                return docs[0];
            }

            const existing = docs.find(
                (doc) => doc.id === current.id
            );

            return existing ?? docs[0];

        });

    } catch (error) {

        console.error("Failed to load documents:", error);

    }
};

    //----------------------------------------
    // Restore Session
    //----------------------------------------

    useEffect(() => {
        const savedMessages = localStorage.getItem(CHAT_STORAGE_KEY);
        const savedDocument = localStorage.getItem(DOCUMENT_STORAGE_KEY);

        if (savedMessages) {
            setMessages(JSON.parse(savedMessages));
        }

        if (savedDocument) {
            const parsed = JSON.parse(savedDocument);

            // Restore the saved document information
            setDocumentInfo(parsed);
        }

        loadDocuments();
    }, []);

    //----------------------------------------
    // Save Chat
    //----------------------------------------

    useEffect(() => {
        localStorage.setItem(
            CHAT_STORAGE_KEY,
            JSON.stringify(messages)
        );
    }, [messages]);

    //----------------------------------------
    // Save Document
    //----------------------------------------

    useEffect(() => {
        if (documentInfo) {
            localStorage.setItem(
                DOCUMENT_STORAGE_KEY,
                JSON.stringify(documentInfo)
            );
        }
    }, [documentInfo]);

    //----------------------------------------
    // Upload PDF
    //----------------------------------------

    const handleUpload = async (file) => {
        setUploading(true);

        try {
            const result = await uploadPDF(file);

            setDocumentInfo(result);

            await loadDocuments();

            const uploadedDocument = {
            id: result.document.id,
            name: result.document.name,
            pages: result.pages,
            chunks: result.chunks,
            embeddings: result.embeddings,
        };

setSelectedDocument(uploadedDocument);

            setMessages([]);
            setQuestion("");

            localStorage.removeItem(CHAT_STORAGE_KEY);

            localStorage.setItem(
                DOCUMENT_STORAGE_KEY,
                JSON.stringify(result)
            );

            showNotification(
                "success",
                "Document uploaded and indexed successfully."
            );
        } catch (error) {
            console.error(error);

            showNotification(
                "error",
                "Failed to upload the document."
            );
        } finally {
            setUploading(false);
        }
    };

    //----------------------------------------
    // Submit Question
    //----------------------------------------

    const handleSubmit = async (query = question) => {
        if (!query.trim()) return;

        if (!selectedDocument) {
            showNotification(
                "warning",
                "Please select a document first."
            );
            return;
        }

        setLoading(true);
        setQuestion("");

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
            const response = await askQuestion(
                query,
                selectedDocument.id
            );

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
            console.error(error);

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

            showNotification(
                "error",
                "Failed to contact the backend."
            );
        } finally {
            setLoading(false);
        }
    };

    //----------------------------------------
// Suggestions
//----------------------------------------

const handleSuggestionClick = async (suggestion) => {
    setQuestion(suggestion);
    await handleSubmit(suggestion);
};

//----------------------------------------
// Active Document
//----------------------------------------

const activeDocument = selectedDocument
    ? {
          document: {
              id: selectedDocument.id,
              name: selectedDocument.name,
          },
          pages: selectedDocument.pages,
          chunks: selectedDocument.chunks,
          embeddings: selectedDocument.embeddings,
      }
    : documentInfo;

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

        <UploadBox onUpload={handleUpload} />

        <DocumentSidebar
            documents={documents}
            selectedDocument={selectedDocument}
            onSelectDocument={setSelectedDocument}
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

        <DocumentInfo documentInfo={activeDocument} />

        <FinancialDashboard
            selectedDocument={selectedDocument}
        />

        <ComparisonWorkspace
            documents={documents}
        />

        <ExportChat
        messages={messages}
        documentInfo={activeDocument}
        />

        <ChatWindow
            messages={messages}
            documentInfo={activeDocument}
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