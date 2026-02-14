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

        def print_task(task):
            print(
                f"[{task['id']}][{task['status']}][{task['category']}][{task['description']}]"
            )

        for task in self.data:
            if filter_by == 1:
                print_task(task)
            elif filter_by == 2:
                if task["status"] == "pending":
                    print_task(task)
            elif filter_by == 3:
                if task["status"] == "completed":
                    print_task(task)
            elif filter_by == 4:
                print("Categories:")
                categories = []
                list_number = 0
                for task in self.data:
                    if task["category"] not in categories:
                        categories.append(task["category"])
                        list_number = list_number + 1
                        print(f"{list_number}. {task["category"]}")

                category_choice = int(input())

                if category_choice <= len(categories):
                    for task in self.data:
                        if task["category"] == list(categories)[category_choice - 1]:
                            print_task(task)
                else:
                    print("Invalid input")
                    raise ValueError(f"Input must be between 1 and {len(categories)}")
                break
            else:
                print("Invalid input")
                raise ValueError("Input must be between 1 and 5")

    def generate_summary(self):
        total_tasks = len(self.data)
        completed_tasks = 0
        pending_tasks = 0
        for task in self.data:
            if task["status"] == "completed":
                completed_tasks = completed_tasks + 1
            elif task["status"] == "pending":
                pending_tasks = pending_tasks + 1
        print(f"Total tasks: {total_tasks}")
        print(f"Completed: {completed_tasks}")
        print(f"Pending: {pending_tasks}")
