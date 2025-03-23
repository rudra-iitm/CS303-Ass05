tasks = []

def add_task(task):
    if task:
        tasks.append(task)
        print(f'Task "{task}" added.')
    else:
        print("Cannot add an empty task.")

def list_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f'{idx}. {task}')

def main():
    while True:
        print("\nOptions: 1. Add Task  2. List Tasks  3. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            task = input("Enter task: ").strip()
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()