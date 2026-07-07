function SourceList({ sources }) {
    if (!sources || sources.length === 0) {
        return null;
    }

    return (
        <div className="source-list">

            <h2>Sources</h2>

            <ul>
                {sources.map((source, index) => (
                    <li key={index}>
                        <strong>Chunk ID:</strong> {source.chunk_id}
                        {" | "}
                        <strong>Score:</strong> {source.score.toFixed(4)}
                    </li>
                ))}
            </ul>

        </div>
    );
}

export default SourceList;