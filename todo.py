import json
import os

FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)


def show_tasks():
    return load_tasks()


def clear_tasks():
    save_tasks([])