import json
import os

FILE_NAME = "memory.json"

def load_memory():
    if not os.path.exists(FILE_NAME):
        return {}

    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_memory(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def remember(key, value):
    data = load_memory()
    data[key] = value
    save_memory(data)

def recall(key):
    data = load_memory()
    return data.get(key)