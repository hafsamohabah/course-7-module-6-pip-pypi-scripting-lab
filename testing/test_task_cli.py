
from lib.task_cli import TaskManager


def test_add_and_complete_task(tmp_path):
    tasks_file = tmp_path / "tasks.json"
    manager = TaskManager(tasks_file)

    task = manager.add_task("Hafsa", "Complete Python lab")

    assert task["id"] == 1
    assert task["description"] == "Complete Python lab"
    assert task["completed"] is False

    # Reload from disk to verify persistence.
    manager = TaskManager(tasks_file)
    tasks = manager.list_tasks("Hafsa")
    assert len(tasks) == 1

    completed = manager.complete_task("Hafsa", 1)
    assert completed["completed"] is True

    # Verify the completed status was saved.
    manager = TaskManager(tasks_file)
    assert manager.list_tasks("Hafsa")[0]["completed"] is True


def test_user_cannot_complete_another_users_task(tmp_path):
    manager = TaskManager(tmp_path / "tasks.json")
    manager.add_task("Hafsa", "My task")

    result = manager.complete_task("OtherUser", 1)

    assert result is None
    assert manager.list_tasks("Hafsa")[0]["completed"] is False
