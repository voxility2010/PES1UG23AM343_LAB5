# Inventory System Code Analysis

## Overview

This project focuses on improving the **code quality, security, and style** of a Python-based inventory system.
An original implementation was analyzed, refactored, and evaluated using industry-standard static analysis tools.

---

## Objectives

* Improve code readability and maintainability
* Identify and fix potential security vulnerabilities
* Ensure adherence to Python coding standards (PEP8)
* Generate detailed analysis reports

---

## Project Structure

```
PES1UG23AM343_LAB5/
│
├── inventory_system.py          # Original code (with issues)
├── clean_inventory_system.py   # Refactored and improved code
├── pylint_report.txt           # Code quality analysis report
├── bandit_report.txt           # Security vulnerability report
├── flake8_report.txt           # Style and formatting report
└── README.md                   # Project documentation
```

---

## Tools Used

### 🔹 Pylint

* Evaluates code quality
* Detects errors and code smells
* Provides an overall score

### 🔹 Bandit

* Identifies security vulnerabilities
* Highlights unsafe coding practices

### 🔹 Flake8

* Ensures compliance with PEP8
* Checks formatting and style issues

---

## Setup & Installation

Install required tools:

```bash
pip install pylint bandit flake8
```

---

## How to Run

Run the following commands to generate reports:

```bash
pylint clean_inventory_system.py > pylint_report.txt

bandit -r clean_inventory_system.py -f text -o bandit_report.txt

flake8 clean_inventory_system.py > flake8_report.txt
```

---

## Workflow

1. Analyze the original code (`inventory_system.py`)
2. Refactor and improve it → `clean_inventory_system.py`
3. Run static analysis tools
4. Review generated reports
5. Improve code based on feedback

---

## Key Learnings

* Writing clean and maintainable Python code
* Using static analysis tools effectively
* Understanding code quality metrics
* Identifying and fixing security issues
* Following PEP8 coding standards

---

## Future Improvements

* Add unit testing using `pytest`
* Automate analysis using CI/CD pipelines
* Extend functionality of the inventory system
* Improve performance and scalability

---

## Conclusion

This project demonstrates how static analysis tools can significantly enhance the **quality, security, and maintainability** of a software system.

---

## Author

* Vardha Kathuria

---
