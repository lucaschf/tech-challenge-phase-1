# Order Management API

## Description

This is an Order Management API designed to help businesses manage their order efficiently.

## Table of Contents

<!-- TOC -->
* [Order Management API](#order-management-api)
  * [Description](#description)
  * [Table of Contents](#table-of-contents)
  * [Technologies](#technologies)
  * [Installation](#installation)
      * [1.Clone the Repository](#1clone-the-repository)
      * [2. Setup Virtual Environment with Poetry (Only if not using Docker Compose)](#2-setup-virtual-environment-with-poetry-only-if-not-using-docker-compose)
      * [3. Install Dependencies (Only if not using Docker Compose)](#3-install-dependencies-only-if-not-using-docker-compose)
      * [4. Setup Environment Variables](#4-setup-environment-variables)
  * [Execution](#execution)
    * [Make (Only if not using Docker Compose)](#make-only-if-not-using-docker-compose)
    * [Docker Compose](#docker-compose)
  * [Project Structure](#project-structure)
  * [Usage](#usage)
    * [General Commands](#general-commands)
    * [Setup and Installation](#setup-and-installation)
    * [Linting](#linting)
    * [Code Complexity and Quality](#code-complexity-and-quality)
    * [Development and Testing](#development-and-testing)
<!-- TOC -->

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
* Docker

## Installation

#### 1.Clone the Repository

The first step is to clone the repository to your local environment.
This can be done using the `git clone` command followed by the repository URL.

```bash
git clone https://github.com/lucaschf/tech-challenge-phase-1.git
```

#### 2. Setup Virtual Environment with Poetry (Only if not using Docker Compose)

Poetry is a tool for dependency management and packaging in Python.
Ensure that Poetry is installed on your system.
Then, create a virtual environment for the project using the command.

```bash
poetry env use 3.12.*
poetry shell
```

see [python-poetry.org](https://python-poetry.org/docs/configuration/) for more information
about poetry.

#### 3. Install Dependencies (Only if not using Docker Compose)

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
| .env      | production         |
| .env      | development        |
| .env.test | test               |

The necessary variables
to be placed in the `.env` files should be defined in the `Settings` class in
the `src.config.env_settings` module.
This class accepts default values, so in cases where default values are enough, you do not
need to define these variables in the `.env` file.

An example of the `.env` file is provided in the `.env.example` file.

## Execution

### Make (Only if not using Docker Compose)

Use the make dev command to run the API server in development mode.

```bash
 make dev
 ```

### Docker Compose

Alternatively, you can use Docker Compose to run the application:

1. Build the image:

```bash
docker-compose build
```

2. Run the container:

```bash
docker-compose up
```

## Project Structure

The project follows the hexagonal architecture, promoting flexibility and testability by decoupling
business logic from specific implementation details. Below, we detail the directory structure and
the role of each component:

- `src`: Root directory of the project's source code.
    - `core`: Heart of the application, containing the business logic and domain rules.
        - `application`  Orchestrates the system's actions.
            - `use_cases`: Use cases that define user interactions with the system and coordinate
              the execution of business rules.
        - `domain`: Model of the problem domain, independent of technical details.
            - `base`:  Base classes and utilities that support domain entities.
            - `entities`: Representations of real-world objects relevant to the domain, with their
              attributes and behaviors.
            - `exceptions`: Custom exceptions that capture violations of business rules,
              facilitating error handling.
            - `repositories`:Interfaces that define how domain entities are persisted and retrieved,
              allowing the replacement of the data storage implementation without affecting the
              domain.
            - `value_objects`: Immutable objects that represent domain concepts, such as money,
              dates, or documents.
        - `adapter`:Adapters that connect the domain to external technologies.
            - `driven`: Adapters that the system uses, such as databases, messaging services, or
              external APIs.
            - `driver`:Adapters that use the system, such as user interfaces, REST APIs, or CLIs.
                - `api`: Implementation of the system's REST API.
                    - `controllers`: Controllers that receive HTTP requests, interact with use
                      cases, and return responses.
                    - `routers`: Routers that define the API routes and connect them to the
                      controllers.
                    - `schemas`: Pydantic models that define the request and response data
                      structures.
                    - `types`: Pydantic models that define custom types used in the schemas.
        - `config`: Project configurations, such as database connection strings, API keys, and other
          environment variables.
- `tests`: Directory containing the project's automated tests.
    - (Subdirectories and test files organized in a mirrored fashion to the code structure in src,
      to facilitate the location and maintenance of tests.)

This hexagonal structure offers several advantages:

- `Testability`: Business logic is isolated, facilitating the creation of unit and integration
  tests.
- `Flexibility`: The replacement of technologies is facilitated, as business rules do not depend
  on implementation details.
- `Maintainability`: The separation of responsibilities makes the code more organized and easier to
  understand, facilitating the maintenance and evolution of the system.
- `Reliability`:Automated tests ensure that the system works as expected, even after code
  modifications.

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

- **`make dev`**: Runs the api server.
  It starts the server with uvicorn, allowing auto-reload on changes.

- **`make test`**: Runs tests in the test environment.
  It uses pytest for testing and coverage for
  generating reports.

- **`make test-cov`**: Runs tests and generates a detailed coverage report.

