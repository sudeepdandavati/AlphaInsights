import "../styles/Comparison.css";

function ComparisonSelector({
    documents,
    selectedDocuments,
    setSelectedDocuments,
    onCompare,
}) {

    const handleToggle = (document) => {

        const exists = selectedDocuments.some(
            (item) => item.id === document.id
        );

        if (exists) {

            setSelectedDocuments(
                selectedDocuments.filter(
                    (item) => item.id !== document.id
                )
            );

        } else {

            setSelectedDocuments([
                ...selectedDocuments,
                document,
            ]);

        }

    };

    return (

        <div className="comparison-selector">

            <h2 className="comparison-title">
                📑 Compare Financial Reports
            </h2>

            {documents.length === 0 ? (

                <p className="comparison-empty">
                    Upload at least one report to begin comparing.
                </p>

            ) : (

                <>
                    <div className="comparison-list">

                        {documents.map((document) => {

                            const checked = selectedDocuments.some(
                                (item) => item.id === document.id
                            );

                            return (

                                <label
                                    key={document.id}
                                    className="comparison-item"
                                >

                                    <input
                                        type="checkbox"
                                        checked={checked}
                                        onChange={() =>
                                            handleToggle(document)
                                        }
                                    />

                                    <div className="comparison-details">

                                        <span className="comparison-name">
                                            {document.name}
                                        </span>

                                        <span className="comparison-meta">
                                            {document.pages} pages • {document.chunks} chunks
                                        </span>

                                    </div>

                                </label>

                            );

                        })}

                    </div>

                    <button
                        className="compare-button"
                        onClick={onCompare}
                        disabled={selectedDocuments.length < 2}
                    >
                        Compare Selected (
                        {selectedDocuments.length}
                        )
                    </button>
                </>

            )}

        </div>

    );

}

export default ComparisonSelector;