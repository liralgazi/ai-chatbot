import json
from pathlib import Path

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
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    messages: list[dict]


def load_business_info() -> dict:
    file_path = Path("data/business_info.json")
    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def build_system_prompt(business_info: dict) -> str:
    services_text = ", ".join(business_info["services"])

    prompt = f"""
You are a customer support assistant for {business_info["business_name"]}.

Business information:
- Monthly membership: {business_info["membership_price"]}
- Personal training: {business_info["personal_training_price"]}
- Sunday to Thursday hours: {business_info["opening_hours"]["sunday_to_thursday"]}
- Friday hours: {business_info["opening_hours"]["friday"]}
- Saturday: {business_info["opening_hours"]["saturday"]}
- Location: {business_info["location"]}
- Services: {services_text}
- Contact email: {business_info["contact_email"]}

Rules:
- Be friendly and professional
- Keep answers short and clear
- Answer only based on the business information above
- If you do not know the answer, say: "I'm not sure about that. Please contact us at {business_info["contact_email"]}."
"""
    return prompt.strip()


@app.get("/")
def root():
    return {"status": "Backend running 🚀"}


@app.post("/chat")
def chat(request: ChatRequest):
    business_info = load_business_info()
    system_prompt = build_system_prompt(business_info)

    messages = [
        {"role": "system", "content": system_prompt},
        *request.messages
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    reply = response.choices[0].message.content

    return {"reply": reply}