🚀 AI Chatbot (Fullstack)

A fullstack AI-powered customer support chatbot built with:

FastAPI (Python) — backend API
OpenAI API — AI responses
React + Vite — frontend UI
✨ Features
Real-time chat interface
Business-specific assistant (Gym example)
Modern UI with chat bubbles
Enter to send messages
Backend + frontend integration
🧠 How it works
User sends message from React UI
Request goes to FastAPI backend
Backend sends prompt to OpenAI
AI response is returned to frontend
Chat updates in real-time
📁 Project Structure
ai-chatbot/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── .env
└── frontend/
    ├── src/
    ├── package.json
    └── ...
⚙️ Setup Instructions
1. Clone the repo
git clone https://github.com/liralgazi/ai-chatbot.git
cd ai-chatbot
2. Backend setup
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Create .env file:

OPENAI_API_KEY=your_api_key_here

Run backend:

uvicorn app:app --reload
3. Frontend setup
cd frontend
npm install
npm run dev
🌐 Usage

Open:

http://localhost:5173

Start chatting with the AI assistant.

⚠️ Notes
.env is not included for security reasons
This is a prototype — chat memory is shared globally (will be improved)
💡 Future Improvements
Per-user chat sessions
Database for chat history
Connect to real business data (RAG)
Deploy to cloud (Render / Vercel)
👩‍💻 Author

Lir Algazi