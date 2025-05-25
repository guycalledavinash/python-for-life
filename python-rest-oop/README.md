# Python Plugin Framework for Data Workflows

A modular Python-based plugin system inspired by ETL tools like FME. This project demonstrates how to design reusable, testable components for data transformation workflows, with support for REST API integration and CI automation.

## 📌 Project Overview

This framework allows you to define processing plugins using Python's object-oriented features and run them as part of a customizable pipeline. It includes:

- A base class for plugin standardization
- Example plugins for string processing
- A REST API client for data fetch/post
- Unit tests with `pytest`
- CI automation using GitHub Actions
- Linting and formatting checks with `flake8` and `black`

## 🛠 Features

- **Object-Oriented Design**: Clean plugin interface using abstract base classes
- **REST API Integration**: Sample client fetches input and sends back results
- **Customizable Workflows**: Chain multiple plugins in any order
- **CI/CD Ready**: Includes automated testing, linting, and formatting checks
- **Containerized Environment**: Docker support for local testing (optional)

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/python-projects.git
cd python-projects
```
### 2. Set up environment
```
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```
### 3. Run the app
```
python main.py
```
### 4. Run tests
```
pytest
```
