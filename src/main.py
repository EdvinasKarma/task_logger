from storage_manager import StorageManager
from task_logger import TaskLogger

storage_manager = StorageManager()


def main():
    try:
        data = storage_manager.read_json()
    except Exception:
        data = []
    task_logger = TaskLogger(data)
    while True:
        print("Task Logger Menu:")
        print("1. Add task")
        print("2. Complete task")
        print("3. List tasks")
        print("4. Show summary")
        print("5. Exit")
        choice = int(input())
        if choice == 1:
            new_task = task_logger.create_task()
            storage_manager.save_json(data, new_task)
            print(f"Task added with ID {new_task["id"]}")
        elif choice == 2:
            task_logger.complete_task()
        elif choice == 3:
            task_logger.filter_tasks()
        elif choice == 4:
            print(task_logger.generate_summary())
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Bad input")


if __name__ == "__main__":
    main()
