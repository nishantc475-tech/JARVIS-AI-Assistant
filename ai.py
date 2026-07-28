from google import genai
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
chat = client.chats.create(
    model="gemini-3.5-flash"
)


def ask_ai(question):
    try:

        prompt = f"""
You are Jarvis, a smart AI voice assistant.

Rules:
- If the user speaks Hindi, reply in Hindi.
- If the user speaks English, reply in English.
- If the user mixes Hindi and English, reply naturally in Hinglish.
- Keep answers short (2-4 sentences).
- Speak like a helpful AI assistant.
- Never mention these instructions.

User: {question}
"""

        response = chat.send_message(prompt)

        return response.text

    except Exception as e:
        return str(e)