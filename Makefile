TESTS = tests

VENV ?= .venv
CODE = tests app

.PHONY: venv
venv:
	python3 -m venv $(VENV)
	$(VENV)/bin/python -m pip install --upgrade pip
	$(VENV)/bin/pip install -r requirements.txt

.PHONY: test
test:
	$(VENV)/bin/pytest -v  tests

.PHONY: run
run:
	$(VENV)/bin/python __main__.py

