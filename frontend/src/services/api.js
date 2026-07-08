import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000";

/**
 * Ask a question about the currently indexed document.
 */
export async function askQuestion(question, topK = 3) {
    try {
        const response = await axios.post(`${API_BASE_URL}/ask`, {
            question,
            top_k: topK,
        });

        return response.data;
    } catch (error) {
        console.error("API Error:", error);
        throw error;
    }
}

/**
 * Upload a PDF to the backend for ingestion.
 */
export async function uploadPDF(file) {
    try {
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
    } catch (error) {
        console.error("Upload Error:", error);
        throw error;
    }
}