function Message({ response }) {
    if (!response) {
        return null;
    }

    return (
        <div className="message">

            <h2>Answer</h2>

            <p>{response.answer}</p>

        </div>
    );
}

export default Message;