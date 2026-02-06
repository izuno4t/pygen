.PHONY: help install dev test test-cov lint format typecheck check clean run run-prod migrate migrate-new

help:
	@printf "\033[36m💡 Available commands:\033[0m\n"
	@echo "  make install    - Install production dependencies"
	@echo "  make dev        - Install all dependencies (including dev)"
	@echo "  make test       - Run tests"
	@echo "  make lint       - Run linter"
	@echo "  make format     - Format code"
	@echo "  make typecheck  - Run type checker"
	@echo "  make check      - Run all checks (lint, typecheck, test)"
	@echo "  make run        - Run development server"
	@echo "  make run-prod   - Run production server"
	@echo "  make migrate    - Run database migrations"
	@echo "  make clean      - Remove build artifacts"

install:
	uv sync

dev:
	uv sync --dev
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
	uv run uvicorn src.project_name.main:app --reload --host 0.0.0.0 --port 8000

run-prod:
	uv run uvicorn src.project_name.main:app --host 0.0.0.0 --port 8000 --workers 4

migrate:
	uv run alembic upgrade head

migrate-new:
	@read -p "Migration message: " msg; \
	uv run alembic revision --autogenerate -m "$$msg"

clean:
	rm -rf .pytest_cache .mypy_cache .ruff_cache htmlcov .coverage
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
