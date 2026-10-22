
# Python Automation Lab

A Python project demonstrating file I/O, API integration, dependency management, and an object-oriented command-line task manager.

## Features

- Generate dated log files using `generate_log()`.
- Fetch a sample post from a public API using `requests`.
- Save API results to `fetched_post.txt`.
- Add, list, and complete user tasks through a CLI.
- Store tasks persistently in `tasks.json`.
- Track Python dependencies in `requirements.txt`.

## Requirements

- Python 3
- pip
- Internet connection for API fetching

## Setup

Clone the repository and enter its directory.

Create and activate a virtual environment on Ubuntu/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Generate a log

```bash
python -c "from lib.generate_log import generate_log; generate_log(['User logged in', 'Report exported'])"
```

The function creates a file named `log_YYYYMMDD.txt` in the current directory.

## Fetch API data

```bash
python lib/fetch_data.py
```

The retrieved post is saved to `fetched_post.txt`.

## Manage tasks

Add a task:

```bash
python lib/task_cli.py add-task --user Hafsa --description "Complete Python lab"
```

List a user's tasks:

```bash
python lib/task_cli.py list-tasks --user Hafsa
```

Complete a task by ID:

```bash
python lib/task_cli.py complete-task --user Hafsa --task-id 1
```

Tasks are saved in `tasks.json`.

## Run tests

```bash
python -m pytest -v
```

## Dependencies

Dependencies are listed in `requirements.txt`. To regenerate this file after installing packages, run:

```bash
python -m pip freeze > requirements.txt
```

## Git workflow

The feature branch for this lab is `feature-automation-tool`.
