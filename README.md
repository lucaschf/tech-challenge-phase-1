# Order Management API

<!-- TOC -->
* [Order Management API](#order-management-api)
  * [Description](#description)
  * [Features](#features)
  * [Project Structure](#project-structure)
  * [Technologies](#technologies)
  * [Installation](#installation)
  * [Running the Application](#running-the-application)
  * [Usage](#usage)
  * [API Documentation](#api-documentation)
<!-- TOC -->

## Description

This Order Management API is designed to help businesses manage their order processes efficiently.
It provides features for product management,
customer management, order processing, and payment integration.

## Features

* **Product Management:** Create, read, update, and delete products.
* **Customer Management:** Create, read, and find customers by CPF.
* **Order Management:** Create, read, list, and update orders.
* **Payment Integration:** Process payments using a simulated payment gateway.

## Project Structure

* **`src`:** Source code of the project.
    * **`core`:** Business logic and domain rules.
        * **`use_cases`:** Defines user interactions and coordinates business rules.
        * **`domain`:** Problem domain model.
            * **`base`:** Base classes and utilities.
            * **`entities`:** Real-world object representations.
            * **`exceptions`:** Custom exceptions.
            * **`repositories`:** Interfaces for persistence and retrieval.
            * **`value_objects`:** Immutable objects representing domain concepts.
    * **`api`:** REST API implementation.
        * **`controllers`:** Handles HTTP requests.
        * **`presenters`:** Transforms use case results to API responses.
        * **`routers`:** Defines API routes.
        * **`schemas`:** Defines request and response structures.
        * **`types`:** Defines custom types.
    * **`config`:** Project configurations.
    * **`payment`:** Payment gateway integration.
* **`tests`:** Automated tests.

## Technologies

* Python 3.12
* FastAPI
* Poetry
* Make
* PostgreSQL
* SQLAlchemy
* Pydantic-settings
* Ruff
* Pytest
* Docker
* Alembic

## Installation

First, clone the repository: `git clone https://github.com/lucaschf/tech-challenge-phase-1.git`

**Option 1: Using Docker Compose (Recommended)**

1. Ensure you have Docker and Docker Compose installed.
2. Set up environment variables:
    * Copy `.env.example` to `.env` and fill in the values.
    * Use the env `DB_HOST=db`.

**Option 2: Setting up Locally**

1. Create a virtual environment (optional, but recommended):
    * `poetry shell`
2. Install dependencies: `make install`
3. Set up environment variables:
    * Copy `.env.example` to `.env` and fill in the values.
   * Use the real database host for the env `DB_HOST`.

## Running the Application

**Option 1: Using Docker Compose**

1. Start the containers: `make up`
   * use `make up build=true` to rebuild the images.

Once the containers are running, the API will be accessible at `http://0.0.0.0:80`.

**Option 2: Setting up Locally**

1. Run the database migrations: `make migrate-db`
2. Start the development server: `make dev`
   3.The API will be accessible at `http://localhost:8000`.

## Usage

Use the `make` command to run common tasks:

* **`make help`:** Show available commands.
* **`make install`:** Install necessary dependencies and set up hooks.
* **`make lint-check`:** Lint source files without modifying them.
* **`make lint-fix`:** Format and fix linting issues in source files.
* **`make lint-check-tests`:** Lint test files without modifying them.
* **`make lint-fix-tests`:** Format and fix linting issues in test files.
* **`make cc`:** Check code complexity.
* **`make dev`:** Run the development server.
* **`make docker-build`:** Build the Docker image.
* **`make docker-up`:** Run the Docker container.
* **`make migrate-db`:** Migrate the database.
* **`make up`:** Run the Docker container with or without build.
* **`make test`:** Run tests.
* **`make test-cov`:** Run tests and generate a coverage report.

## API Documentation

After running the application, you can access the interactive API documentation at
`http://localhost:8000/DOCS_URL` (e.g., `http://localhost:8000/docs`).

Additionally, you can access the ReDoc documentation at
`http://localhost:8000/REDOC_URL` (e.g., `http://localhost:8000/redoc`).
