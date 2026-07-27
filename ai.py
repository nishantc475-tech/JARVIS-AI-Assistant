from google import genai
from dotenv import load_dotenv
import os

# .env file load karega
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def ask_ai(question):
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=f"Answer in 2-3 short sentences: {question}"
        )

        return response.text

    except Exception as e:
        return str(e)