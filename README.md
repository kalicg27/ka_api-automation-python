# API Automation Framework (Python + pytest)

The main goal is to show how I organise API tests in a clean and maintainable way.
This repository contains an API test automation framework written in Python, using `pytest` and `requests`.  
The framework is designed to be easily adapted to any REST API by changing configuration values, and demonstrates how I approach test structure, maintainability, and reporting.

## Tech Stack

- Python 3.10+
- pytest
- requests
- python-dotenv
- pydantic
- pytest-html (for reporting)
- GitHub Actions (CI)

## Project Goals

- Demonstrate clean API test automation structure in Python
- Show usage of:
  - Reusable API client classes
  - Configuration and environments
  - Data-driven tests
  - Response validation with models
  - Continuous Integration with GitHub Actions

The sample implementation targets the public API at `https://reqres.in`, but the framework can be pointed to any REST API.

## Project Structure

```text
src/
  config/
    settings.py        # Environment and base URL configuration
  clients/
    users_client.py    # API client for /users endpoints
  models/
    user_models.py     # Pydantic models for requests/responses
  utils/
    data_loader.py     # Helper utilities (to be extended)

tests/
  conftest.py          # Shared pytest fixtures
  test_users_get.py    # Tests for GET /users
  test_users_create.py # Tests for POST /users
  test_users_negative.py (planned)

data/
  create_user_payload.json

reports/
  (HTML or Allure reports can be generated here)
