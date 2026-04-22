from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI

load_dotenv()
client = OpenAI()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

messages = [
    {
        "role": "system",
        "content": """
You are a customer support assistant for FitZone Gym.

Business information:
- Monthly membership: $50
- Personal training session: $30
- Opening hours: Sunday to Thursday, 6:00 AM to 10:00 PM
- Friday: 6:00 AM to 4:00 PM
- Saturday: Closed
- Location: Tel Aviv
- Services: gym access, group classes, personal training
- Contact: fitzone@email.com

Rules:
- Be friendly and professional
- Keep answers short and clear
- Answer only based on the business information above
- If you do not know the answer, say: "I’m not sure about that. Please contact us at fitzone@email.com."
"""
    }
]

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"status": "ok", "message": "FitZone backend is running"}

@app.post("/chat")
def chat(request: ChatRequest):
    messages.append({"role": "user", "content": request.message})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})

    return {"reply": reply}