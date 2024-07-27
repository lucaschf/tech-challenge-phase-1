.DEFAULT_GOAL := help

help:
	@sed -n 's/^## //p' $(MAKEFILE_LIST) | column -t -s ':' | sed -e 's/^/ /'

# Directories
SRC_DIRS := src
TEST_DIRS := tests

# Xenon configuration
XENON_MAX_ABSOLUTE := B
XENON_MAX_MODULES := B
XENON_MAX_AVERAGE := B

## install: Install necessary dependencies and set up hooks.
install:
	@ poetry install  # Install Python dependencies using Poetry
	@ pre-commit install  # Set up Git pre-commit hooks
	@ gitlint install-hook  # Install Gitlint hook for linting commits

## lint-check: Lint source files without modifying them.
lint-check:
	@ ruff check $(SRC_DIRS)

## lint-fix: Format and fix linting issues in source files.
lint-fix:
	@ ruff check $(SRC_DIRS) --fix
	@ ruff format $(SRC_DIRS)

## lint-check-tests: Lint test files without modifying them.
lint-check-tests:
	@ ruff check $(TEST_DIRS)

## lint-fix-tests: Format and fix linting issues in test files.
lint-fix-tests:
	@ ruff check $(TEST_DIRS) --fix
	@ ruff format $(TEST_DIRS)

## cc: Calculate Cyclomatic Complexity.
cc:
	# Calculating cyclomatic complexity using radon
	@ radon cc $(SRC_DIRS) -s

	# Ensuring code complexity adheres to standards using xenon
	@ xenon --max-absolute $(XENON_MAX_ABSOLUTE) \
	       --max-modules $(XENON_MAX_MODULES) \
	       --max-average $(XENON_MAX_AVERAGE) $(SRC_DIRS)

## dev: Run the development server.
dev:
	set -e &&export ENVIRONMENT='development' && uvicorn $(SRC_DIRS).api:app --host 0.0.0.0 --reload

## docker-build: Build the Docker image.
docker-build:
	@ docker-compose build

## docker-up: Run the Docker container.
docker-up:
	@ docker-compose up

## migrate-db: Migrate the database.
migrate-db:
	@ alembic upgrade head

## up: Run the Docker container with or without build.
up:
	@ if [ "$(build)" = "true" ]; then \
		$(MAKE) docker-build; \
	fi; \
	$(MAKE) docker-up

## test: Run tests.
test:
	set -e &&export ENVIRONMENT='test' && alembic upgrade head && coverage run -m pytest --ff $(extra) && coverage report

## test-cov: Run tests and generate a coverage report.
test-cov:
	set -e &&export ENVIRONMENT='test' && coverage run -m pytest --capture=no &&coverage report &&coverage html


.PHONY: help install lint-check lint-fix lint-check-tests lint-fix-tests cc dev run docker-build docker-up migrate-db up test test-cov
