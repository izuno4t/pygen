.PHONY: help install dev test test-cov lint format typecheck check clean run

help:
	@printf "\033[36m💡 Available commands:\033[0m\n"
	@echo "  make install    - Install production dependencies"
	@echo "  make dev        - Install all dependencies (including dev)"
	@echo "  make test       - Run tests"
	@echo "  make test-cov   - Run tests with coverage"
	@echo "  make lint       - Run linter"
	@echo "  make format     - Format code"
	@echo "  make typecheck  - Run type checker"
	@echo "  make check      - Run all checks (lint, typecheck, test)"
	@echo "  make run        - Run application"
	@echo "  make clean      - Remove build artifacts"

install:
	uv sync

dev:
	uv sync --extra dev
	uv run pre-commit install

test:
	uv run pytest

test-cov:
	uv run pytest --cov --cov-report=html --cov-report=term-missing

lint:
	uv run ruff check .

format:
	uv run ruff format .
	uv run ruff check --fix .

typecheck:
	uv run mypy .

check: lint typecheck test

run:
	uv run python -m project_name

clean:
	rm -rf .pytest_cache .mypy_cache .ruff_cache htmlcov .coverage
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
