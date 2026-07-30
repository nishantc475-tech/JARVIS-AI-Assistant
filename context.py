# Global context memory

last_pdf = None
last_image = None
last_search = None
last_command = None
last_ai_response = ""


def set_last_pdf(path):
    global last_pdf
    last_pdf = path


def get_last_pdf():
    return last_pdf


def set_last_image(path):
    global last_image
    last_image = path


def get_last_image():
    return last_image


def set_last_search(search):
    global last_search
    last_search = search


def get_last_search():
    return last_search


def set_last_command(command):
    global last_command
    last_command = command


def get_last_command():
    return last_command


def set_last_response(text):
    global last_ai_response
    last_ai_response = text


def get_last_response():
    return last_ai_response