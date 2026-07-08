import { useRef, useState } from "react";
import "../styles/UploadBox.css";

function UploadBox({ onUpload }) {

    const [selectedFile, setSelectedFile] = useState(null);

    const fileInputRef = useRef(null);

    const handleFileChange = (event) => {

        const file = event.target.files[0];

        if (!file) return;

        if (file.type !== "application/pdf") {
            alert("Please choose a PDF file.");
            return;
        }

        setSelectedFile(file);

    };

    const handleUpload = () => {

        if (!selectedFile) {
            alert("Please choose a PDF first.");
            return;
        }

        onUpload(selectedFile);

    };

    return (

        <div className="upload-box">

            <h2>
                📄 Upload Financial Report
            </h2>

            <p className="upload-subtitle">
                Upload an annual report, SEC filing or financial statement.
            </p>

            <input
                ref={fileInputRef}
                type="file"
                accept=".pdf"
                onChange={handleFileChange}
                hidden
            />

            <button
                className="choose-button"
                onClick={() => fileInputRef.current.click()}
            >
                📁 Choose PDF
            </button>

            {selectedFile && (

                <div className="selected-file">

                    <span>📄</span>

                    <span>{selectedFile.name}</span>

                </div>

            )}

            <button
                className="upload-button"
                disabled={!selectedFile}
                onClick={handleUpload}
            >
                🚀 Upload Document
            </button>

        </div>

    );

}

export default UploadBox;