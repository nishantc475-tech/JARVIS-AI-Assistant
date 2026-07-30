import json
import os

FILE_NAME = "schedule.json"


def load_schedule():

    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


def save_schedule(data):

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def add_schedule(task, task_time):

    data = load_schedule()

    data.append({
        "task": task,
        "time": task_time
    })

    save_schedule(data)


def get_schedule():

    return load_schedule()


def remove_schedule(task, task_time):

    data = load_schedule()

    data = [
        item for item in data
        if not (
            item["task"] == task
            and item["time"] == task_time
        )
    ]

    save_schedule(data)