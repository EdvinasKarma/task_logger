from storage_manager import StorageManager
from task_logger import TaskLogger

storage_manager = StorageManager()

def main():
    data = storage_manager.read_json()
    task_logger = TaskLogger(data)
    print("Task Logger Menu:")
    print("1. Add task")
    print("2. Complete task")
    print("3. List tasks")
    print("4. Show summary")
    print("5. Exit")
    choice = int(input())
    if choice == 1:
        task_logger.add_task()
    elif choice == 2:
        task_logger.complete_task()
    elif choice == 3:
        task_logger.filter_tasks()
    elif choice == 4:
        task_logger.generate_summary()
    elif choice == 5:
        print("Goodbye!")
    else:
        print("Bad input")


if __name__ == "__main__":
    main()
