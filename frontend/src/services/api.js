import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000";

// ----------------------------------------
// Upload PDF
// ----------------------------------------

export async function uploadPDF(file) {

    const formData = new FormData();

    formData.append("file", file);

    const response = await axios.post(
        `${API_BASE_URL}/upload`,
        formData,
        {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        }
    );

    return response.data;

}

// ----------------------------------------
// Get all uploaded documents
// ----------------------------------------

export async function getDocuments() {

    const response = await axios.get(
        `${API_BASE_URL}/documents`
    );

    return response.data.documents;

}

// ----------------------------------------
// Get financial metrics
// ----------------------------------------

export async function getFinancialMetrics(documentId) {

    const response = await axios.get(
        `${API_BASE_URL}/documents/${documentId}/metrics`
    );

    return response.data.metrics;

}

// ----------------------------------------
// Compare multiple documents
// ----------------------------------------

export async function compareDocuments(documentIds) {

    const response = await axios.post(
        `${API_BASE_URL}/compare`,
        {
            document_ids: documentIds,
        }
    );

    return response.data;

}

// ----------------------------------------
// Ask Question
// ----------------------------------------

export async function askQuestion(
    question,
    documentId,
    topK = 3
) {

    const response = await axios.post(
        `${API_BASE_URL}/ask`,
        {
            question,
            document_id: documentId,
            top_k: topK,
        }
    );

    return response.data;

}