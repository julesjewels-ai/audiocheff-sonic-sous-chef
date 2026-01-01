.PHONY: install run test clean

VENV_NAME := venv
PYTHON := ./$(VENV_NAME)/bin/python
PIP := ./$(VENV_NAME)/bin/pip

install:
	python3 -m venv $(VENV_NAME)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "Installation complete. Virtual environment created in $(VENV_NAME)."

run:
	@echo "Running AudioCheff in DEMO mode..."
	$(PYTHON) main.py --demo

test:
	$(PYTHON) -m pytest tests/

clean:
	rm -rf $(VENV_NAME)
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +