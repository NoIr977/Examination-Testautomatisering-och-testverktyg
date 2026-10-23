# Examination - Test Automation

This project tests the Läslistan website, where users can save their favorite books to a separate page, add new books to the book list, or simply see all books on the site.

Users can also see statistics about how many books are in the list and how many of them are marked as favorites and added to "Mina böcker".

## Technologies

All tests in this project are written in Python, and the BDD scenarios are written in English.

We have used TDD for backend development and BDD for frontend testing.

We have also used Playwright to automate frontend testing and pytest to run our tests.

For BDD testing, we have used pytest-bdd and Gherkin scenarios.

We have written unit tests and integration tests to check individual parts of the application and how they work together.

## Test Design

The project uses:
- Pytest for unit and integration testing.
- Pytest-BDD with Gherkin for frontend test scenarios.
- Playwright for browser automation.
- Scenario Outline to test book creation with different data.
- Page Object Pattern to separate page interactions from test steps.

The project includes 16 automated tests:
- 8 unit tests
- 2 integration tests
- 6 frontend tests

## Requirements

- Python 3.14 (tested with Python 3.14.5)
- pip

## Installation

1. Clone the repository.
2. Open the project folder.
3. Create and activate a virtual environment.

On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

4. Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

5. Install the Playwright browser:

```bash
python -m playwright install chromium
```

## Run Tests

Run all tests:

```bash
python -m pytest -v
```

Run frontend tests with a visible browser:

```bash
python -m pytest tests/frontend/ -v --headed --slowmo 500
```

## Project Structure

- `src/` – Application classes
- `tests/unit/` – Unit tests
- `tests/integration/` – Integration tests
- `tests/frontend/` – Frontend BDD tests
- `features/` – Gherkin scenarios
- `pages/` – Page Object classes for frontend testing
- `STORIES.md` – User stories
- `ANSWERS.md` – Answers to theory questions
- `requirements.txt` – Python dependencies