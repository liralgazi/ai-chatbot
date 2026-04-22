from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI()

print("AI Chatbot is ready! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a friendly assistant."},
            {"role": "user", "content": user_input}
        ]
    )

    print("Bot:", response.choices[0].message.content)