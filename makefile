PHONY: install test coverage format lint clean build all help

POETRY := poetry
PYTHON := $(POETRY) run python
PYTEST := $(POETRY) run pytest
BLACK := $(POETRY) run black
ISORT := $(POETRY) run isort
FLAKE8 := $(POETRY) run flake8

help: ## Display this help message
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@awk -F ':|##' '/^[^\t].+?:.*?##/ { printf "  %-20s %s\n", $$1, $$NF }' $(MAKEFILE_LIST)

install: ## Install project dependencies
	$(POETRY) install

test: ## Run tests
	$(PYTEST)

coverage: ## Run tests with coverage report
	$(PYTEST) --cov=logic_gates --cov-report=html

format: ## Format code with Black and isort
	$(BLACK) .
	$(ISORT) .

lint: ## Run linting checks
	$(FLAKE8) src tests
	$(BLACK) --check .
	$(ISORT) --check-only .

clean: ## Clean up build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .pytest_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete

build: clean ## Build project
	$(POETRY) build

check: lint test ## Run all checks (linting and tests)

all: clean install format check build ## Run all tasks (clean, install, format, check, build)

run: ## Run the main program
	$(PYTHON) -m logic_gates.gates
