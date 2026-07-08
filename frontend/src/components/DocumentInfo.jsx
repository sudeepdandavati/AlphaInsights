import "../styles/DocumentInfo.css";

function DocumentInfo({ documentInfo }) {

    if (!documentInfo) {
        return null;
    }

    return (
        <div className="document-info">

            <div className="document-header">
                <span className="document-icon">📄</span>

                <div>
                    <h3>{documentInfo.document.name}</h3>
                    <p>Document indexed successfully</p>
                </div>
            </div>

            <div className="document-stats">

                <div className="stat-card">
                    <span className="stat-number">
                        {documentInfo.pages}
                    </span>

                    <span className="stat-label">
                        Pages
                    </span>
                </div>

                <div className="stat-card">
                    <span className="stat-number">
                        {documentInfo.chunks}
                    </span>

                    <span className="stat-label">
                        Chunks
                    </span>
                </div>

                <div className="stat-card">
                    <span className="stat-number">
                        {documentInfo.embeddings}
                    </span>

                    <span className="stat-label">
                        Embeddings
                    </span>
                </div>

            </div>

        </div>
    );
}

export default DocumentInfo;