import "../styles/SourceList.css";

function SourceList({ sources }) {
    if (!sources || sources.length === 0) {
        return null;
    }

    return (
        <div className="source-list">

            <h3 className="source-title">
                📄 Sources
            </h3>

            <div className="source-grid">

                {sources.map((source, index) => (

                    <div
                        key={index}
                        className="source-card"
                    >
                        <span className="source-chunk">
                            📄 Chunk {source.chunk_id}
                        </span>

                        <span className="source-score">
                            {(source.score * 100).toFixed(1)}% Match
                        </span>
                    </div>

                ))}

            </div>

        </div>
    );
}

export default SourceList;