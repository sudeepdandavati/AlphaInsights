import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000";

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