import json

_file_path = "tasks.json"


def read_json(file_path: str):
    try:
        with open(f"{file_path}", "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("File not found")
        raise FileNotFoundError


def write_json(file_path: str, data):
    try:
        with open(f"{file_path}", "w") as file:
            json.dump(data, file, indent=4)
        return None
    except FileNotFoundError:
        print("File not found")
        raise FileNotFoundError
