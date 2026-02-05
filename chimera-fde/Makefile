.PHONY: setup test test-docker

setup:
	uv sync

test:
	uv run pytest tests/ -v

test-docker:
	docker build -t chimera-fde:dev .
	docker run --rm -t chimera-fde:dev pytest