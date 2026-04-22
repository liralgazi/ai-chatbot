import { useState } from "react";
import ChatWindow from "./components/ChatWindow";
import ChatInput from "./components/ChatInput";

function App() {
  const [messages, setMessages] = useState([
    {
      text: "Hi! I'm the FitZone assistant. How can I help you today?",
      sender: "bot",
    },
  ]);

  const [inputValue, setInputValue] = useState("");
  const [isTyping, setIsTyping] = useState(false);

  const sendMessage = async () => {
    const trimmed = inputValue.trim();
    if (!trimmed) return;

    setMessages((prev) => [...prev, { text: trimmed, sender: "user" }]);
    setInputValue("");
    setIsTyping(true);

    try {
      const res = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: trimmed })
      });

      const data = await res.json();

      setMessages((prev) => [
        ...prev,
        { text: data.reply, sender: "bot" }
      ]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { text: "Something went wrong. Please try again.", sender: "bot" }
      ]);
    } finally {
      setIsTyping(false);
    }
  };

  return (
    <div className="page">
      <div className="chat-shell">
        <header className="chat-header">
          <div className="brand">
            <div className="brand-badge">F</div>
            <div>
              <h1>FitZone Assistant</h1>
              <p>Memberships, classes, hours, and services</p>
            </div>
          </div>

          <div className="status-pill">
            <span className="status-dot" />
            Online
          </div>
        </header>

        <ChatWindow messages={messages} isTyping={isTyping} />

        <ChatInput
          value={inputValue}
          onChange={setInputValue}
          onSend={sendMessage}
        />
      </div>
    </div>
  );
}

export default App;