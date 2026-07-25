import os
from google import genai

client = genai.Client(
    api_key=os.getenv("")
)
def ask_ai(question):
    try:
        response = client.models.generate_content(
            model="gemini-flash-lite-latest",
            contents=question,
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"