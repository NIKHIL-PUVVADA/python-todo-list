class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print("No Task.")

    def list_tasks(self):
        if self.tasks:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("No tasks.")

def main():
    todo_list = TodoList()
    
    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task = input("Enter task1: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter task2: ")
            todo_list.remove_task(task)
        elif choice == "3":
            todo_list.list_tasks()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
