import { useRef } from "react";

function ChatInput({ value, onChange, onSend }) {
  const textareaRef = useRef(null);

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      onSend();
    }
  };

  const handleChange = (e) => {
    onChange(e.target.value);

    const textarea = textareaRef.current;
    if (textarea) {
      textarea.style.height = "56px";
      textarea.style.height = `${Math.min(textarea.scrollHeight, 140)}px`;
    }
  };

  return (
    <div className="input-wrapper">
      <div className="input-shell">
        <textarea
          ref={textareaRef}
          value={value}
          onChange={handleChange}
          onKeyDown={handleKeyDown}
          placeholder="Ask about pricing, classes, opening hours..."
          rows="1"
        />
        <button onClick={onSend} className="send-button">
          Send
        </button>
      </div>
      <div className="input-hint">Press Enter to send · Shift + Enter for a new line</div>
    </div>
  );
}

export default ChatInput;