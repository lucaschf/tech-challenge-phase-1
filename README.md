# Order Management API 

## Description

This is an Order Management API designed to help businesses manage their order efficiently.


## Technologies

* Python ~3.12
* FastAPI
* Poetry
* Make
* PostgresSQL
* SqlAlchemy
* Pydantic-settings
* Ruff
* Pytest

## Installation

#### 1.Clone the Repository

The first step is to clone the repository to your local environment.
This can be done using the `git clone` command followed by the repository URL.

```bash
git clone https://github.com/lucaschf/tech-challenge-phase-1.git
```

#### 2. Setup Virtual Environment with Poetry

Poetry is a tool for dependency management and packaging in Python.
Ensure that Poetry is installed on your system.
Then, create a virtual environment for the project using the command.

```bash
poetry env use 3.1*.*
poetry shell
```

see [python-poetry.org](https://python-poetry.org/docs/configuration/) for more information
about poetry.

#### 3. Install Dependencies

Use the `make` command to install all the project dependencies.
The `make install` command is used to install the dependencies listed in the `pyproject.toml` file.

```bash 
make install
```

#### 4. Setup Environment Variables

The project uses different `.env` files for different environments (test, dev, prod).
Create these files at the root of the project and fill them with the necessary variables.

| Env file  | Target environment |
|-----------|--------------------|
| .env      | development        |
| .env.dev  | development        |
| .env.test | test               |
| .env.prod | production         |

As you can see, there are four environment file names accepted.
You can use either `.env.dev` or `.env` to development environment.
But for prod and test environments only one `.env` file name is allowed

The necessary variables
to be placed in the `.env` files should be defined in the `Settings` class in
the `src.core.settings` module.
This class accepts default values, so in cases where default values are sufficient, you do not
need to define these variables in the `.env` files.

An example of the `.env` file is provided in the `.env.example` file.

## Usage

This project uses a Makefile to streamline various development tasks.
Below are the available make commands and their descriptions:

### General Commands

- **`make help`**: Displays help information by parsing this Makefile for targets and descriptions.

### Setup and Installation

- **`make install`**: Installs necessary dependencies and sets up hooks.
  This includes installing Python dependencies using Poetry,
  setting up Git pre-commit hooks, and installing a Gitlint hook for linting commits.

### Linting

- **`make lint-check`**: Lints source files without modifying them.
  It checks the code using ruff, 
- **`make lint-fix`**: Formats and fixes linting issues in source files using the same tools.
- **`make lint-check-tests`**: Lints test files without modifying them.
- **`make lint-fix-tests`**: Formats and fixes linting issues in test files.

### Code Complexity and Quality

- **`make cc`**: Calculates Cyclomatic Complexity using radon and ensures code complexity adheres to
  set standards using xenon.

### Development and Testing

- **`make dev`**: Runs the development server.
  It sets the environment to 'development' and starts
  the server with uvicorn, allowing auto-reload on changes.

- **`make test`**: Runs tests in the test environment.
  It uses pytest for testing and coverage for
  generating reports.

- **`make test-cov`**: Runs tests and generates a detailed coverage report.

### Production

- **`make run`**: Runs the production server.
