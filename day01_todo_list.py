"""
Day 1: Simple Command-Line To-Do List
Part of the "Python Daily Bites" project.

Features:
- Add tasks
- View tasks
- Mark tasks as done
- Delete tasks
- Tasks are saved to a local file (tasks.txt) so they persist between runs
"""

import os

TASKS_FILE = "tasks.txt"


def load_tasks():
    """Read tasks from file into a list of (status, text) tuples."""
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            for line in f:
                line = line.rstrip("\n")
                if not line:
                    continue
                status, text = line.split("|", 1)
                tasks.append([status, text])
    return tasks


def save_tasks(tasks):
    """Write tasks back to file."""
    with open(TASKS_FILE, "w") as f:
        for status, text in tasks:
            f.write(f"{status}|{text}\n")


def show_tasks(tasks):
    if not tasks:
        print("No tasks yet. Add one!")
        return
    for i, (status, text) in enumerate(tasks, start=1):
        mark = "x" if status == "done" else " "
        print(f"[{mark}] {i}. {text}")


def add_task(tasks):
    text = input("Enter new task: ").strip()
    if text:
        tasks.append(["pending", text])
        save_tasks(tasks)
        print("Task added.")
    else:
        print("Task cannot be empty.")


def complete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to mark done: "))
        tasks[num - 1][0] = "done"
        save_tasks(tasks)
        print("Task marked as done.")
    except (ValueError, IndexError):
        print("Invalid task number.")


def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed[1]}")
    except (ValueError, IndexError):
        print("Invalid task number.")


def main():
    tasks = load_tasks()
    menu = """
--- To-Do List ---
1. View tasks
2. Add task
3. Mark task as done
4. Delete task
5. Quit
"""
    while True:
        print(menu)
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()