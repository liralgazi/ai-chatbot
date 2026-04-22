from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

print("AI Chatbot is ready! Type 'exit' to quit.\n")

messages = [
    {"role": "system", "content": "You are a friendly gym assistant. Keep answers short and helpful."}
]

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    reply = response.choices[0].message.content

    print("Bot:", reply)

    # saves the messages into a list - memory 
    messages.append({"role": "assistant", "content": reply})