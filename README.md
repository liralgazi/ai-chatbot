# 🚀 AI Chatbot (Fullstack)

A modern fullstack AI-powered customer support chatbot built with **React**, **FastAPI**, and the **OpenAI API**.

This project simulates a real business assistant that can answer customer questions dynamically based on business data loaded from JSON files.

---

## ✨ Features

- 💬 Real-time AI chat interface
- ⚛️ Modern frontend built with React + Vite
- 🐍 FastAPI backend with Python
- 🤖 OpenAI API integration
- 📁 Dynamic business data using JSON
- 🎨 Responsive modern UI
- ⌨️ Enter-to-send messaging
- 🔄 Frontend ↔ Backend API communication

---

## 🧠 Tech Stack

### Frontend
- React
- Vite
- JavaScript
- CSS

### Backend
- Python
- FastAPI
- OpenAI API
- Pydantic

### Other Tools
- Git & GitHub
- REST APIs
- JSON

---

## 🏗️ How It Works

1. The user sends a message from the React frontend
2. The frontend sends the conversation to the FastAPI backend
3. The backend loads business data from a JSON file
4. A dynamic system prompt is created
5. The backend sends the request to the OpenAI API
6. The AI response is returned to the frontend
7. The chat updates in real-time

---

## 📁 Project Structure

```bash
ai-chatbot/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── data/
│   │   └── business_info.json
│   └── .env
│
└── frontend/
    ├── src/
    │   ├── components/
    │   ├── App.jsx
    │   └── App.css
    ├── package.json
    └── vite.config.js
```

---

# ⚙️ Full Setup Guide

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/liralgazi/ai-chatbot.git
cd ai-chatbot
```

---

## 2️⃣ Backend Setup

Move into the backend folder:

```bash
cd backend
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

### macOS / Linux
```bash
source venv/bin/activate
```

### Windows
```bash
venv\Scripts\activate
```

Install backend dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file inside the `backend` folder:

```env
OPENAI_API_KEY=your_api_key_here
```

Run the backend server:

```bash
uvicorn app:app --reload
```

Backend will run on:

```bash
http://127.0.0.1:8000
```

---

## 3️⃣ Frontend Setup

Open a new terminal and move into the frontend folder:

```bash
cd frontend
```

Install frontend dependencies:

```bash
npm install
```

Run the frontend:

```bash
npm run dev
```

Frontend will run on:

```bash
http://localhost:5173
```

---

# 🌐 Usage

Open the frontend URL in your browser and start chatting with the AI assistant.

Example questions:
- "What are your opening hours?"
- "Do you offer personal training?"
- "How much is the membership?"

---

# 💡 Project Goals

This project was built to practice:

- Fullstack development
- API integration
- AI-powered applications
- React state management
- FastAPI backend development
- Dynamic prompt generation
- Clean architecture separation between frontend, backend, and business data

---

# 🚀 Future Improvements

- User authentication
- Database integration
- Chat history persistence
- Multi-business support
- RAG / document-based chatbot
- Deployment with Vercel & Render

---

# 👩‍💻 Author

**Lir Algazi**

- GitHub: https://github.com/liralgazi
- LinkedIn: https://www.linkedin.com/in/lir-algazi-53804a200/
