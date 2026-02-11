from storage_manager import read_json, _file_path
from task_logger import add_task, complete_task, generate_summary, list_tasks

def main():
    data = read_json(_file_path)
    print("Task Logger Menu:")
    print("1. Add task")
    print("2. Complete task")
    print("3. List tasks")
    print("4. Show summary")
    print("5. Exit")
    choice = int(input())
    if choice == 1:
        add_task(data)
    elif choice == 2:
        complete_task(data)
    elif choice == 3:
        list_tasks(data)
    elif choice == 4:
        generate_summary(data)
    elif choice == 5:
        print("Goodbye!")
    else:
        print("Bad input")

if __name__ == "__main__":
    main()
