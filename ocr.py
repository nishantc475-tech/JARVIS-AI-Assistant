import pytesseract
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def read_image_text():

    root = Tk()
    root.withdraw()

    image_path = askopenfilename(
        title="Select Image",
        filetypes=[
            ("Image Files", "*.png *.jpg *.jpeg *.bmp")
        ]
    )

    if not image_path:
        return "No image selected."

    image = Image.open(image_path)

    text = pytesseract.image_to_string(image)

    if text.strip() == "":
        return "No text found in the image."

    return text