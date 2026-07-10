import { useState } from "react";

import "../styles/SourceList.css";
import SourcePreview from "./SourcePreview";

function SourceList({ sources }) {

    const [selectedSource, setSelectedSource] = useState(null);

    if (!sources || sources.length === 0) {
        return null;
    }

    return (
        <>
            <div className="source-list">

                <h3 className="source-title">
                    📄 Sources
                </h3>

                <div className="source-grid">

                    {sources.map((source, index) => (

                        <button
                            key={index}
                            className="source-card"
                            onClick={() => setSelectedSource(source)}
                        >

                            <span className="source-chunk">
                                📄 Chunk {source.chunk_id}
                            </span>

                            <span className="source-score">
                                {(source.score * 100).toFixed(1)}% Match
                            </span>

                        </button>

                    ))}

                </div>

            </div>

            <SourcePreview
                source={selectedSource}
                onClose={() => setSelectedSource(null)}
            />
        </>
    );
}

export default SourceList;