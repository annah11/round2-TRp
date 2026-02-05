.PHONY: setup test test-docker security

setup:
	uv sync

test:
	uv run pytest tests/ -v

security:
	uv run bandit -r .

test-docker:
	docker build -t chimera-fde:dev .
	docker run --rm -t chimera-fde:dev pytest