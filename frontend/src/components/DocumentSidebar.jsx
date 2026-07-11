import "../styles/DocumentSidebar.css";

function DocumentSidebar({
    documents,
    selectedDocument,
    onSelectDocument,
}) {

    if (!documents.length) {
        return null;
    }

    return (

        <div className="document-sidebar">

            <h2 className="sidebar-title">
                📚 Documents
            </h2>

            <div className="document-list">

                {documents.map((document) => (

                    <div
                        key={document.id}
                        className={`document-item ${
                            selectedDocument?.id === document.id
                                ? "active"
                                : ""
                        }`}
                        onClick={() => onSelectDocument(document)}
                    >

                        <div className="document-icon">
                            📄
                        </div>

                        <div className="document-details">

                            <div className="document-name">
                                {document.name}
                            </div>

                            <div className="document-meta">

                                {document.pages} pages

                                {" • "}

                                {document.chunks} chunks

                            </div>

                        </div>

                    </div>

                ))}

            </div>

        </div>

    );

}

export default DocumentSidebar;