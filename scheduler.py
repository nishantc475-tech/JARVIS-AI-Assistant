import json
import os

FILE_NAME = "schedule.json"


def load_schedule():

    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_schedule(data):

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def add_schedule(task, time):

    data = load_schedule()

    data.append({
        "task": task,
        "time": time
    })

    save_schedule(data)


def get_schedule():

    return load_schedule()