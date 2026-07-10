import "../styles/SourcePreview.css";

function SourcePreview({ source, onClose }) {

    if (!source) return null;

    return (

        <div
            className="preview-overlay"
            onClick={onClose}
        >

            <div
                className="preview-modal"
                onClick={(e) => e.stopPropagation()}
            >

                <div className="preview-header">

                    <div>

                        <h2>📄 Source Preview</h2>

                        <p>
                            Retrieved context used to generate the answer
                        </p>

                    </div>

                    <button
                        className="close-button"
                        onClick={onClose}
                    >
                        ✕
                    </button>

                </div>

                <div className="preview-meta">

                    <div className="meta-card">

                        <span className="meta-label">
                            Document
                        </span>

                        <span className="meta-value">
                            {source.document_name}
                        </span>

                    </div>

                    <div className="meta-card">

                        <span className="meta-label">
                            Chunk
                        </span>

                        <span className="meta-value">
                            {source.chunk_id}
                        </span>

                    </div>

                    <div className="meta-card">

                        <span className="meta-label">
                            Similarity
                        </span>

                        <span className="meta-value">
                            {(source.score * 100).toFixed(1)}%
                        </span>

                    </div>

                </div>

                <div className="context-box">

                    <h3>
                        Retrieved Context
                    </h3>

                    <div className="preview-content">

                        {source.text}

                    </div>

                </div>

            </div>

        </div>

    );

}

export default SourcePreview;