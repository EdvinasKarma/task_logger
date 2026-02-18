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
        while True:
            try:
                id = int(input("ID: "))
                if id > len(self.data) or id == 0:
                    print(f"ID not exist. Available ID's: 1 to {len(self.data)}.")
                    try_again = input("Try again? Y/N - ")
                    if try_again == "Y":
                        continue
                    elif try_again == "N":
                        print("Goodbye!")
                        return None
                break
            except ValueError:
                print("Input should be valid number")

        if self.data[id - 1]["status"] == "completed":
            print("Task already completed")
        else:
            self.data[id - 1]["status"] = "completed"
            storage_manager.write_json(self.data)
            print(f"Task with ID {id} was completed")

    def filter_tasks(self):
        print("Filter:")
        print("1. Show all")
        print("2. Pending")
        print("3. Completed")
        print("4. By category")

        def print_task(task):
            print(
                f"[{task['id']}][{task['status']}][{task['category']}][{task['description']}]"
            )

        while True:
            try:
                filter_by = int(input())
                if filter_by > 5 or filter_by == 0:
                    print("Select one of four filter options")
                    try_again = input("Try again? Y/N - ")
                    if try_again == "Y":
                        continue
                    elif try_again == "N":
                        print("Goodbye!")
                        return None
                break
            except ValueError:
                print("Input should be valid number")

        for task in self.data:
            if filter_by == 1:
                print_task(task)
            elif filter_by == 2:
                if task["status"] == "pending":
                    print_task(task)
            elif filter_by == 3:
                if task["status"] == "completed":
                    print_task(task)
        if filter_by == 4:
            print("Categories:")
            categories = []
            category_list_number = 0
            for task in self.data:
                if task["category"] not in categories:
                    categories.append(task["category"])
                    category_list_number = category_list_number + 1
                    print(f"{category_list_number}. {task['category']}")

            while True:
                try:
                    category_choice = int(input())
                    if category_choice > len(categories) or category_choice == 0:
                        print("Select a category from the list")
                        try_again = input("Try again? Y/N - ")
                        if try_again == "Y":
                            continue
                        elif try_again == "N":
                            print("Goodbye!")
                            return None
                    break
                except ValueError:
                    print("Input should be valid number")

            for task in self.data:
                if task["category"] == list(categories)[category_choice - 1]:
                    print_task(task)

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
