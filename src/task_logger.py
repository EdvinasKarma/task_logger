from datetime import datetime
from storage_manager import storage_manager


class TaskLogger:
    def __init__(self, data: list):
        self.data = data

    def add_task(self):
        description = input("Description: ")
        category = input("Category: ")

        new_id = len(self.data) + 1
        new_task = {
            "id": new_id,
            "description": description,
            "category": category,
            "status": "pending",
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        self.data.append(new_task)
        storage_manager.write_json(self.data)

        print(f"Task added with ID {new_id}")

    def complete_task(self):
        id = int(input("ID: "))
        self.data[id - 1]["status"] = "completed"

        storage_manager.write_json(self.data)

        print(f"Task with ID {id} was completed")

    def filter_tasks(self):
        print("Filter:")
        print("1. Show all")
        print("2. Pending")
        print("3. Completed")
        print("4. By category")

        filter_by = int(input())

        if filter_by == 1:
            for task in self.data:
                print(
                    f"[{task['id']}][{task['status']}][{task['category']}][{task['description']}]"
                )
        elif filter_by == 2:
            for task in self.data:
                if task["status"] == "pending":
                    print(
                        f"[{task['id']}][{task['status']}][{task['category']}][{task['description']}]"
                    )
        elif filter_by == 3:
            for task in self.data:
                if task["status"] == "completed":
                    print(
                        f"[{task['id']}][{task['status']}][{task['category']}][{task['description']}]"
                    )
        elif filter_by == 4:
            print("Categories:")
            categories = set()
            for task in self.data:
                categories.add(task["category"])

            for list_number, category in enumerate(categories, start=1):
                print(f"{list_number}. {category}")

            category_choice = int(input())

            if category_choice <= len(categories):
                for task in self.data:
                    if task["category"] == list(categories)[category_choice - 1]:
                        print(
                            f"[{task['id']}][{task['status']}][{task['category']}][{task['description']}]"
                        )
        else:
            print("Invalid input")

    def generate_summary(self):
        total_tasks = len(self.data)
        completed_tasks = 0
        for task in self.data:
            if task["status"] == "completed":
                completed_tasks = completed_tasks + 1
        pending_tasks = 0
        for task in self.data:
            if task["status"] == "pending":
                pending_tasks = pending_tasks + 1
        print(f"Total tasks: {total_tasks}")
        print(f"Completed: {completed_tasks}")
        print(f"Pending: {pending_tasks}")
