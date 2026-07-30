from tkinter import Tk
from tkinter.filedialog import askopenfilename


def choose_image():

    root = Tk()
    root.withdraw()

    file_path = askopenfilename(
        title="Select Image",
        filetypes=[
            ("Image Files", "*.png *.jpg *.jpeg *.webp")
        ]
    )

    if not file_path:
        return None

    return file_path