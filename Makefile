PYTHON ?= python

.PHONY: install test lint demo

install:
	$(PYTHON) -m pip install -e "./python[dev]"

test:
	pytest -q python/tests

lint:
	ruff check python

demo:
	sleepband inspect data/example_recording.csv
	sleepband evaluate data/evaluation_example.csv
