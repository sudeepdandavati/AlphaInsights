import { useState } from "react";

import "./App.css";

import ChatBox from "./components/ChatBox";
import Message from "./components/Message";
import SourceList from "./components/SourceList";

function App() {
    const [response, setResponse] = useState(null);

    return (
        <div className="app">

            <h1>AlphaInsights</h1>

            <p>
                Ask questions about your financial report using AI.
            </p>

            <ChatBox onResponse={setResponse} />

            <Message response={response} />

            <SourceList sources={response?.sources} />

        </div>
    );
}

export default App;