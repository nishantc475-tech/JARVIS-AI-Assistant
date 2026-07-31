from google import genai
from config import GEMINI_API_KEY, AI_MODELS
from context import set_last_response

client = genai.Client(api_key=GEMINI_API_KEY)


def ask_ai(question):

    prompt = f"""
You are Jarvis, an intelligent personal AI assistant created by Nishant.

Rules:
- Be friendly, confident and professional.
- Reply in the same language as the user.
- Keep answers short (2–4 sentences) unless the user asks for a detailed explanation.
- Avoid markdown formatting like **bold**, *, or bullet points unless requested.
- Do not mention that you are an AI model.
- Sound natural like a real assistant.

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

            answer = response.text

            set_last_response(answer)

            return answer

        except Exception as e:

            print(f"{model} failed -> {e}")

            last_error = e

            continue

    error = str(last_error)

    if "503" in error:
        return "Gemini servers are busy right now. Please try again in a few minutes."

    if "10054" in error:
        return "Internet connection was interrupted. Please try again."

    return f"AI Error: {error}"