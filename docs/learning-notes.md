# 📚 Learning Notes

These are concepts I learned while building Sentinel.

---

# Linux

## mkdir

Creates a directory (folder).

Example:

mkdir docs

---

## touch

Creates an empty file.

Example:

touch settings.py

---

## cd

Changes the current directory.

Example:

cd app/config

---

## ls

Lists the contents of a directory.

Example:

ls

---

## rm

Deletes a file.

Example:

rm file.txt

---

## rm -r

Deletes a directory and everything inside it.

Example:

rm -r old_folder

---

# Git

## git add

Stages changes for the next commit.

## git commit

Creates a snapshot of the staged changes.

## git push

Uploads commits to GitHub.

## git pull

Downloads changes from GitHub.

---

# Python

## Package

A folder containing an `__init__.py` file.

## Module

A single Python file.

Example:

settings.py

## Virtual Environment

An isolated Python environment for a project.

---

# UV

A modern Python package manager.

Common commands:

uv add package_name

uv run python app.py

uv sync

---

# Project Lessons

## Why settings.py exists

Instead of calling `os.getenv()` everywhere, the application loads configuration once and shares it with every module.

## Why __init__.py exists

It tells Python that a directory should be treated as a package, making imports work cleanly.


# pyproject.toml

The pyproject.toml file defines a Python project.

It contains:

- Project name
- Version
- Description
- Python version requirement
- Dependencies

Modern Python tools such as uv and pip read this file to understand how the project is configured.


## Virtual Environment (.venv)

A virtual environment is an isolated Python environment for one project.

Why use it?

- Prevents dependency conflicts.
- Keeps project packages separate from system packages.
- Makes projects reproducible.

Activate:

```bash
source .venv/bin/activate
```

Deactivate:

```bash
deactivate
```

## pip

pip is Python's package installer.

Examples:

Install a package:

```bash
python3 -m pip install requests
```

Show installed packages:

```bash
python3 -m pip list
```

Export dependencies:

```bash
python3 -m pip freeze > requirements.txt
```

Using `python3 -m pip` is often more reliable than just `pip` because it guarantees you're using the pip associated with the current Python interpreter.


## Virtual Environment

A virtual environment contains its own:

- Python interpreter
- Installed packages
- pip

When activated:

```bash
source .venv/bin/activate
```

The `python` command refers to the interpreter inside the virtual environment instead of the system Python.

# python3 -m venv

Creates an isolated Python environment.

Example:

```bash
python3 -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

Deactivate:

```bash
deactivate
```

Benefits:

- Keeps project dependencies isolated.
- Prevents conflicts with system Python.
- Makes projects reproducible.

## Class

A class groups related data and behavior together.

Example:

```python
class Settings:
    app_name = "Sentinel"
```

Think of a class as a blueprint or template for organizing related information.

## python vs python3

On many Linux systems, `python` is not installed by default.

Instead, Python 3 is accessed using:

python3

Inside a virtual environment, `python` points to the virtual environment's Python interpreter.

Best practice:
- Outside a virtual environment: use `python3`
- Inside a virtual environment: use `python`

## Python imports

There is a difference between importing a module and importing an object.

Example:

from app.config import settings

imports the `settings.py` module.

from app.config.settings import settings

imports the `settings` object that was created with:

settings = Settings()

Python projects commonly expose objects this way for easier reuse across the application.


## Running Python files vs modules

Running:

python tests/test_settings.py

executes the file directly, which changes Python's import path.

Running:

python -m tests.test_settings

executes the module as part of the project package, preserving package imports.

For larger projects, prefer `python -m` when running tests.
