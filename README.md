# Flaky Tests Project

This is a sample Python project to demonstrate running Pytest with GitHub Actions, including intentional flaky tests.

## Installation

```bash
pip install -r requirements.txt
```

## Running Tests

```bash
pytest
```

## GitHub Actions

The tests run automatically: - On every push to main - On every pull request to main - Every 4 hours via a scheduled GitHub Action

Test results are stored as JUnit XML artifacts.

````yaml
---

## **Deployment Steps**
1. Create a **new GitHub repository** and clone it:
   ```bash
   git clone https://github.com/YOUR_USERNAME/flaky-tests-project.git
   cd flaky-tests-project
````
