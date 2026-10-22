
import argparse
import json
from pathlib import Path


TASKS_FILE = Path("tasks.json")


class TaskManager:
    """Manage tasks stored in a JSON file."""

    def __init__(self, filename=TASKS_FILE):
        self.filename = Path(filename)
        self.tasks = self._load_tasks()

    def _load_tasks(self):
        """Load saved tasks, or start with an empty list."""
        if not self.filename.exists():
            return []

        with self.filename.open("r", encoding="utf-8") as file:
            return json.load(file)

    def _save_tasks(self):
        """Save the current tasks to a JSON file."""
        with self.filename.open("w", encoding="utf-8") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, username, description):
        """Add a task to a user's account."""
        task_id = max(
            (task["id"] for task in self.tasks),
            default=0,
        ) + 1

        task = {
            "id": task_id,
            "username": username,
            "description": description,
            "completed": False,
        }

        self.tasks.append(task)
        self._save_tasks()

        print(f"Task {task_id} added for {username}: {description}")
        return task

    def complete_task(self, username, task_id):
        """Mark one of the user's tasks as complete."""
        for task in self.tasks:
            if task["id"] == task_id and task["username"] == username:
                if task["completed"]:
                    print(f"Task {task_id} is already complete.")
                    return task

                task["completed"] = True
                self._save_tasks()
                print(f"Task {task_id} marked as complete.")
                return task

        print(f"Task {task_id} was not found for {username}.")
        return None

    def list_tasks(self, username):
        """Display all tasks belonging to a user."""
        user_tasks = [
            task for task in self.tasks
            if task["username"] == username
        ]

        if not user_tasks:
            print(f"No tasks found for {username}.")
            return user_tasks

        for task in user_tasks:
            status = "Complete" if task["completed"] else "Pending"
            print(
                f"[{task['id']}] {task['description']} - {status}"
            )

        return user_tasks


def main():
    """Parse commands and run the requested task action."""
    parser = argparse.ArgumentParser(
        description="Manage tasks from the command line."
    )
    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    add_parser = subparsers.add_parser(
        "add-task",
        help="Add a task for a user",
    )
    add_parser.add_argument("--user", required=True)
    add_parser.add_argument("--description", required=True)

    complete_parser = subparsers.add_parser(
        "complete-task",
        help="Mark a task as complete",
    )
    complete_parser.add_argument("--user", required=True)
    complete_parser.add_argument("--task-id", type=int, required=True)

    list_parser = subparsers.add_parser(
        "list-tasks",
        help="List tasks for a user",
    )
    list_parser.add_argument("--user", required=True)

    args = parser.parse_args()
    manager = TaskManager()

    if args.command == "add-task":
        manager.add_task(args.user, args.description)
    elif args.command == "complete-task":
        manager.complete_task(args.user, args.task_id)
    elif args.command == "list-tasks":
        manager.list_tasks(args.user)


if __name__ == "__main__":
    main()
