# Examination - Test Automation

This project tests the Läslistan website, where users can save their favorite books to a separate page, add new books to the book list, or simply see all books on the site.

Users can also see statistics about how many books are in the list and how many of them are marked as favorites and added to "Mina böcker".

## Technologies

All tests in this project are written in Python, and the BDD scenarios are written in English.

We have used TDD for backend development and BDD for frontend testing.

We use Playwright for frontend browser automation and pytest for unit and integration tests.

For frontend BDD testing, we use Behave and Gherkin scenarios.

We have written unit tests and integration tests to check individual parts of the application and how they work together.

## Test Design

The project uses:

- Pytest for unit and integration testing.
- Behave with Gherkin for frontend test scenarios.
- Playwright for browser automation.
- Scenario Outline to test book creation with different data.
- Page Object Pattern to separate page interactions from test steps.
- Dependency Injection to connect BookStore with FavoriteBooks.
- Mock objects to test BookStore separately.

The project includes 16 automated tests:

- 8 unit tests
- 2 integration tests
- 6 frontend BDD scenarios

## Requirements

- Python 3.14 (tested with Python 3.14.5)
- pip
- pytest 9.1.1
- behave 1.3.3
- playwright 1.64.0

All required Python packages are listed in `requirements.txt`.

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

Run unit and integration tests:

```bash
python -m pytest tests/unit/ tests/integration/ -v
```

Run all frontend BDD scenarios:

```bash
python -m behave
```

Run a specific frontend feature:

```bash
python -m behave features/catalog.feature
```

All frontend scenarios run in headless Chromium by default.

## Project Structure

- `src/` – Application classes
- `tests/unit/` – Unit tests
- `tests/integration/` – Integration tests
- `features/` – Gherkin scenarios
- `features/steps/` – Behave step definitions
- `features/environment.py` – Playwright browser setup and cleanup
- `pages/` – Page Object classes for frontend testing
- `STORIES.md` – User stories
- `ANSWERS.md` – Answers to theory questions
- `requirements.txt` – Python dependencies