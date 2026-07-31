from datetime import datetime


HISTORY_FILE = "chat_history.txt"


def save_chat(sender, message):

    with open(
        HISTORY_FILE,
        "a",
        encoding="utf-8"
    ) as file:

        time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        file.write(
            f"[{time}] {sender}: {message}\n"
        )


def clear_history():

    with open(
        HISTORY_FILE,
        "w",
        encoding="utf-8"
    ):
        pass


def load_history():

    try:

        with open(
            HISTORY_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()

    except FileNotFoundError:

        return ""