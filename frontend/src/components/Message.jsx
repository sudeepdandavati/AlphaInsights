import "../styles/Message.css";

function Message({ response }) {
    if (!response) return null;

    return (
        <div className="message">
            <p className="message-text">
                {response.answer}
            </p>
        </div>
    );
}

export default Message;