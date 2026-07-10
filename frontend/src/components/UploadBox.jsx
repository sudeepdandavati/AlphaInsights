import { useRef, useState } from "react";
import "../styles/UploadBox.css";

function UploadBox({ onUpload }) {

    const [selectedFile, setSelectedFile] = useState(null);
    const [dragActive, setDragActive] = useState(false);

    const fileInputRef = useRef(null);

    const validateFile = (file) => {

        if (!file) return;

        if (file.type !== "application/pdf") {
            alert("Please choose a PDF file.");
            return;
        }

        setSelectedFile(file);
    };

    const handleFileChange = (event) => {
        validateFile(event.target.files[0]);
    };

    const handleUpload = () => {

        if (!selectedFile) {
            alert("Please choose a PDF first.");
            return;
        }

        onUpload(selectedFile);
    };

    const handleDragOver = (event) => {
        event.preventDefault();
        setDragActive(true);
    };

    const handleDragLeave = () => {
        setDragActive(false);
    };

    const handleDrop = (event) => {

        event.preventDefault();

        setDragActive(false);

        const file = event.dataTransfer.files[0];

        validateFile(file);
    };

    return (

        <div
            className={`upload-box ${dragActive ? "drag-active" : ""}`}
            onDragOver={handleDragOver}
            onDragLeave={handleDragLeave}
            onDrop={handleDrop}
        >

            <h2>
                📄 Upload Financial Report
            </h2>

            <p className="upload-subtitle">
                Drag & Drop your PDF here
                <br />
                or choose a file below.
            </p>

            <input
                ref={fileInputRef}
                type="file"
                accept=".pdf"
                hidden
                onChange={handleFileChange}
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