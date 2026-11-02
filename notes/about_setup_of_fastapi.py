"""
4. WHAT IS FASTAPI?
===================

FastAPI is a modern, high-performance Python web framework
used to build APIs and backend applications.

It helps developers create REST APIs with automatic
documentation, data validation and support for asynchronous
programming.


WHY FASTAPI?
-----------

1. High Performance:
   FastAPI provides high performance and is suitable for
   building scalable backend applications.

2. Automatic API Documentation:
   Automatically generates interactive API documentation
   using Swagger UI and ReDoc.

3. Data Validation:
   Uses Pydantic to validate incoming request data.

4. Python Type Hints:
   Supports Python type hints for better code readability,
   validation and editor support.

5. Asynchronous Programming:
   Supports async and await for handling asynchronous
   operations.

6. Database Integration:
   Can integrate with databases such as MySQL,
   PostgreSQL and MongoDB.

7. Dependency Injection:
   Provides a dependency injection system to manage
   reusable components and shared resources.

8. Authentication Support:
   Supports security tools and authentication workflows
   such as OAuth2.


INSTALLATION
------------

Install FastAPI with its standard optional dependencies:

    pip install "fastapi[standard]"

This installs FastAPI along with commonly used tools
such as Uvicorn.


RUNNING THE APPLICATION
-----------------------

Command:

    uvicorn main:app --reload

Explanation:

    uvicorn:
        ASGI server used to run the FastAPI application.

    main:
        Python file name (main.py).

    app:
        FastAPI application instance created inside main.py.

    --reload:
        Automatically restarts the server when code changes
        are detected.

Example:

    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/")
    def home():
        return {"message": "Hello FastAPI"}

After running the command, open:

    http://127.0.0.1:8000

Interactive documentation:

    http://127.0.0.1:8000/docs


5. WHAT IS A VIRTUAL ENVIRONMENT (venv)?
=========================================

A virtual environment is an isolated Python environment
that allows each project to maintain its own dependencies
and package versions.

It prevents dependency conflicts between different
Python projects.


WHY DO WE NEED A VIRTUAL ENVIRONMENT?
-------------------------------------

Imagine working on two different projects.

PROJECT A:

    FastAPI version: 0.115
    Pydantic version: 2.x

PROJECT B:

    FastAPI version: 0.120
    Other dependency versions

If packages are installed globally, different projects
may require incompatible versions of the same package.

This can create dependency conflicts.

A virtual environment solves this problem by keeping
each project's dependencies isolated.


ADVANTAGES OF VIRTUAL ENVIRONMENTS
----------------------------------

1. Dependency Isolation:
   Each project maintains its own installed packages.

2. Version Management:
   Different projects can use different package versions.

3. Avoids Dependency Conflicts:
   Packages installed in one project do not interfere
   with packages installed in another project.

4. Reproducibility:
   Dependencies can be recorded in a requirements.txt
   file so the environment can be recreated.

5. Clean Development Environment:
   Avoids unnecessary global package installations.


CREATING A VIRTUAL ENVIRONMENT
------------------------------

Python provides a built-in module called venv.

Command:

    python -m venv .venv

Explanation:

    python:
        Runs the Python interpreter.

    -m:
        Executes a Python module as a script.

    venv:
        Python's built-in virtual environment module.

    .venv:
        Name of the virtual environment directory.


ACTIVATING THE VIRTUAL ENVIRONMENT
----------------------------------

WINDOWS CMD:

    .venv\Scripts\activate

WINDOWS POWERSHELL:

    .venv\Scripts\Activate.ps1

LINUX / macOS:

    source .venv/bin/activate

After activation, the terminal usually displays:

    (.venv)

This indicates that the virtual environment is active.


INSTALLING FASTAPI
------------------

After activating the virtual environment:

    pip install "fastapi[standard]"

The packages will be installed inside the active
virtual environment instead of the global Python
environment.


CHECKING INSTALLED PACKAGES
---------------------------

Command:

    pip list

Displays the packages installed in the active
Python environment.


DEACTIVATING THE VIRTUAL ENVIRONMENT
------------------------------------

Command:

    deactivate

This exits the active virtual environment and returns
to the system's default Python environment.


CHECKING THE PYTHON INTERPRETER
-------------------------------

WINDOWS CMD:

    where python

LINUX / macOS:

    which python

When the virtual environment is activated, the Python
executable should point to the project's .venv directory.


6. DIFFERENCE BETWEEN PYTHON, pip AND venv
===========================================

PYTHON:
    Programming language and interpreter used to
    execute Python programs.

pip:
    Python package installer used to install,
    upgrade and manage Python packages.

venv:
    Python module used to create isolated
    virtual environments.

FASTAPI:
    Python web framework used to build APIs.

UVICORN:
    ASGI server used to run FastAPI applications.

PYDANTIC:
    Python library used for data validation
    and serialization.


7. KEY TAKEAWAYS
================

1. API enables communication between software applications.

2. Client sends requests and the server processes them
   and returns responses.

3. HTTP is the communication protocol used by clients
   and servers.

4. Endpoints are specific URLs used for API operations.

5. JSON is a common format for exchanging data.

6. HTTP methods define the operations to perform.

7. Status codes communicate the result of a request.

8. FastAPI is a modern Python framework for developing APIs.

9. Virtual environments isolate project dependencies.

10. Uvicorn runs FastAPI applications as an ASGI server.

11. Pydantic validates and serializes application data.


BEST PRACTICE
-------------

Create a separate virtual environment for every Python
project and install its dependencies inside that environment.

This helps maintain clean, isolated and reproducible
development environments.

"""