import MessageBubble from "./MessageBubble";

function ChatWindow({ messages, isTyping }) {
  return (
    <main className="chat-box">
      {messages.map((msg, i) => (
        <MessageBubble key={i} text={msg.text} sender={msg.sender} />
      ))}
      {isTyping && <div className="typing">FitZone assistant is typing...</div>}
    </main>
  );
}

export default ChatWindow;