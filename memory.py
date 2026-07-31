import json
import os

FILE_NAME = "memory.json"

def load_memory():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

def save_memory(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def remember(key, value):
    data = load_memory()
    data[key] = value
    save_memory(data)

def recall(key):
    data = load_memory()
    return data.get(key, None)

def clear_memory():
    save_memory({})

def recall_all():
    return load_memory()    

def forget(key):
    data = load_memory()

    if key in data:
        del data[key]
        save_memory(data)
        return True

    return False