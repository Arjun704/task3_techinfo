import pickle

# Step 2: Define a Task class with attributes (title, description, status)
class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.status = "Incomplete"

    def mark_as_complete(self):
        self.status = "Complete"

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nStatus: {self.status}\n"

# Step 3: Define a ToDolist class with methods
class ToDoList:
    def __init__(self):
        self.tasks = []

    # Method to add a new task to the list
    def add_task(self, title, description):
        new_task = Task(title, description)
        self.tasks.append(new_task)

    # Method to delete a task from the list
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Invalid task index.")

    # Method to view current tasks
    def view_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"Task {index + 1}:\n{task}")

    # Method to save tasks to a file
    def save_tasks(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.tasks, file)

    # Method to load tasks from a file
    def load_tasks(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.tasks = pickle.load(file)
        except FileNotFoundError:
            print("File not found. No tasks loaded.")

# Step 6: Test the app
if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("\nMenu:")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. View tasks")
        print("4. Save tasks to a file")
        print("5. Load tasks from a file")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)
        elif choice == "2":
            index = int(input("Enter the index of the task to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            filename = input("Enter the filename to save tasks: ")
            todo_list.save_tasks(filename)
        elif choice == "5":
            filename = input("Enter the filename to load tasks from: ")
            todo_list.load_tasks(filename)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
