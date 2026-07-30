from pypdf import PdfReader
from ai import ask_ai
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def read_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        if text.strip() == "":
            return "No readable text found in the PDF."

        return text

    except Exception as e:
        return str(e)


def summarize_pdf(pdf_path):

    text = read_pdf(pdf_path)

    if (
        "No readable text" in text
        or "No such file" in text
        or len(text.strip()) == 0
    ):
        return text

    # Gemini ko bahut zyada text mat bhejo
    text = text[:6000]

    prompt = f"""
You are Jarvis.

Read the following PDF content and provide a clear and concise summary.

PDF Content:

{text}
"""

    return ask_ai(prompt)


def choose_pdf():

    root = Tk()
    root.withdraw()

    file_path = askopenfilename(
        title="Select PDF",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if not file_path:
        return None

    return file_path