import json


class StorageManager:
    def __init__(self, file_path: str = "tasks.json"):
        self.file_path = file_path

    def read_json(self) -> list[dict]:
        try:
            with open(f"{self.file_path}", "r") as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            raise

    def write_json(self, data):
        with open(f"{self.file_path}", "w") as file:
            json.dump(data, file, indent=4)
        return None


storage_manager = StorageManager()
