function MessageBubble({ text, sender }) {
  const isUser = sender === "user";

  return (
    <div className={`message-row ${isUser ? "message-row-user" : "message-row-bot"}`}>
      <div className={`message-bubble ${isUser ? "message-user" : "message-bot"}`}>
        {text}
      </div>
    </div>
  );
}

export default MessageBubble;