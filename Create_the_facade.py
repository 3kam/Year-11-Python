import json  # For saving and loading tasks as JSON data
from datetime import datetime  # For handling and formatting deadlines
import os  # For checking if the JSON file already exists

# === Represents a single task ===
class Task:
    def __init__(self, task, category, deadline):
        # Store the task info and convert deadline string to a date object (format: DD-MM-YYYY)
        self.task = task
        self.category = category
        self.deadline = datetime.strptime(deadline, "%d-%m-%Y")

    def __str__(self):
        # How the task is displayed when printed
        return f"Task: {self.task}, Category: {self.category}, Deadline: {self.deadline.strftime('%d-%m-%Y')}"

    def to_dict(self):
        # Convert task to dictionary for saving in JSON
        return {
            "task": self.task,
            "category": self.category,
            "deadline": self.deadline.strftime("%d-%m-%Y")
        }

    @staticmethod
    def from_dict(data):
        # Create Task object from dictionary when loading from JSON
        return Task(data["task"], data["category"], data["deadline"])


# === Manages tasks (add, edit, delete, load, save) ===
class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.tasks = []  # List of task objects
        self.filename = filename  # Filename to save/load tasks
        self.load_tasks()  # Load tasks on startup

    def add_task(self, task, category, deadline):
        # Add a new task and save all tasks
        new_task = Task(task, category, deadline)
        self.tasks.append(new_task)
        self.save_tasks()
        return new_task

    def get_tasks(self):
        # Return list of tasks
        return self.tasks

    def edit_task(self, index, new_task, new_category, new_deadline):
        # Update a task and save changes
        self.tasks[index].task = new_task
        self.tasks[index].category = new_category
        self.tasks[index].deadline = datetime.strptime(new_deadline, "%d-%m-%Y")
        self.save_tasks()

    def delete_task(self, index):
        # Remove a task and save changes
        removed = self.tasks.pop(index)
        self.save_tasks()
        return removed

    def save_tasks(self):
        # Write tasks to JSON file
        with open(self.filename, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def load_tasks(self):
        # Read tasks from JSON file if it exists
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(item) for item in data]


# === Facade to simplify user interactions ===
class ToDoListFacade:
    def __init__(self):
        self.task_manager = TaskManager()

    def add_task(self):
        # Get user input for a new task, validate date, then add
        task = input("Enter task description: ")
        category = input("Enter category (e.g. Work, Personal): ")
        deadline = input("Enter deadline (DD-MM-YYYY): ")
        try:
            # Validate date is today or later
            deadline_date = datetime.strptime(deadline, "%d-%m-%Y")
            today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
            if deadline_date < today:
                print("Invalid date. Deadline must be today or in the future.")
                return

            self.task_manager.add_task(task, category, deadline)
            print("Task added successfully.")
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY.")

    def list_tasks(self):
        # List all tasks, or message if none
        tasks = self.task_manager.get_tasks()
        if not tasks:
            print("No tasks to display.")
            return
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

    def edit_task(self):
        # List tasks and let user update one, validating date input
        self.list_tasks()
        try:
            index = int(input("Enter the number of the task to edit: ")) - 1
            new_task = input("Enter new description: ")
            new_category = input("Enter new category: ")
            new_deadline = input("Enter new deadline (DD-MM-YYYY): ")

            deadline_date = datetime.strptime(new_deadline, "%d-%m-%Y")
            today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
            if deadline_date < today:
                print("Invalid date. Deadline must be today or in the future.")
                return

            self.task_manager.edit_task(index, new_task, new_category, new_deadline)
            print("Task updated successfully.")
        except (IndexError, ValueError):
            print("Invalid input. Please check the task number and date format.")

    def delete_task(self):
        # List tasks and delete selected one
        self.list_tasks()
        try:
            index = int(input("Enter the number of the task to delete: ")) - 1
            removed = self.task_manager.delete_task(index)
            print(f"Task '{removed.task}' deleted successfully.")
        except (IndexError, ValueError):
            print("Invalid input. Please enter a valid task number.")


# === Main menu to interact with user ===
def main():
    todo = ToDoListFacade()
    while True:
        print("\n=== To-Do List Menu ===")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Choose an option: ")
        if choice == "1":
            todo.add_task()
        elif choice == "2":
            todo.list_tasks()
        elif choice == "3":
            todo.edit_task()
        elif choice == "4":
            todo.delete_task()
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")


# Only run the program if this file is executed directly
if __name__ == "__main__":
    main()
