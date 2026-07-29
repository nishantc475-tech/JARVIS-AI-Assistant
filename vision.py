from google import genai
from PIL import Image
from screen import capture_screen

from config import GEMINI_API_KEY, MODEL_NAME

client = genai.Client(api_key=GEMINI_API_KEY)


def describe_image(image_path):

    try:

        image = Image.open(image_path)

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=[
                "Describe this image in detail.",
                image
            ]
        )

        return response.text

    except Exception as e:
        return str(e)

def describe_screen():
    try:
        image_path = capture_screen()
        return describe_image(image_path)

    except Exception as e:
        return str(e)