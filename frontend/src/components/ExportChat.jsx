import "../styles/ExportChat.css";

import { exportAsMarkdown } from "../utils/exportChat";

function ExportChat({

    messages,

    documentInfo,

}) {

    if (!messages || messages.length === 0) {
        return null;
    }

    return (

        <div className="export-chat">

            <button
                className="export-button"
                onClick={() =>
                    exportAsMarkdown(
                        messages,
                        documentInfo
                    )
                }
            >

                💾 Export Conversation

            </button>

        </div>

    );

}

export default ExportChat;