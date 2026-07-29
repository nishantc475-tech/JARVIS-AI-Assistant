import json
import os

FILE = "reminders.json"


def load_reminders():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r") as f:
        return json.load(f)


def save_reminders(reminders):
    with open(FILE, "w") as f:
        json.dump(reminders, f, indent=4)


def add_reminder(reminder):
    reminders = load_reminders()
    reminders.append(reminder)
    save_reminders(reminders)


def show_reminders():
    return load_reminders()


def clear_reminders():
    save_reminders([])