from google import genai
from config import GEMINI_API_KEY, AI_MODELS
from context import set_last_response

client = genai.Client(api_key=GEMINI_API_KEY)


def ask_ai(question):

    prompt = f"""
You are Jarvis, an intelligent personal AI assistant created by Nishant.

Be friendly, professional and concise.

User:
{question}
"""

    last_error = None

    for model in AI_MODELS:

        try:

            response = client.models.generate_content(
                model=model,
                contents=prompt
            )

            set_last_response(response.text)

            return response.text

        except Exception as e:

            print(f"{model} failed -> {e}")

            last_error = e

            continue

    return f"All AI models failed.\n{last_error}"