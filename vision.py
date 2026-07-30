from google import genai
from PIL import Image
from screen import capture_screen

from config import GEMINI_API_KEY, AI_MODELS

client = genai.Client(api_key=GEMINI_API_KEY)


def describe_image(image_path):

    try:

        image = Image.open(image_path)

        last_error = None

        for model in AI_MODELS:

            try:

                response = client.models.generate_content(
                    model=model,
                    contents=[
                        "Describe this image in detail.",
                        image
                    ]
                )

                return response.text

            except Exception as e:

                print(f"{model} failed -> {e}")
                last_error = e

        error = str(last_error)

        if "503" in error:
            return "Gemini servers are busy. Please try again after a few minutes."

        if "10054" in error:
            return "Connection interrupted. Please check your internet and try again."

        return error

    except Exception as e:
        return str(e)


def describe_screen():

    try:

        image_path = capture_screen()

        return describe_image(image_path)

    except Exception as e:

        return str(e)