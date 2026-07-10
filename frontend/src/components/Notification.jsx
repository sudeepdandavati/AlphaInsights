import { useEffect } from "react";
import "../styles/Notification.css";

function Notification({
    type = "success",
    message,
    onClose,
}) {

    useEffect(() => {

        if (!message) return;

        const timer = setTimeout(() => {
            onClose();
        }, 3500);

        return () => clearTimeout(timer);

    }, [message, onClose]);

    if (!message) return null;

    return (

        <div className={`notification ${type}`}>

            <span className="notification-icon">

                {type === "success" && "✅"}

                {type === "error" && "❌"}

                {type === "warning" && "⚠️"}

            </span>

            <span className="notification-message">

                {message}

            </span>

        </div>

    );

}

export default Notification;