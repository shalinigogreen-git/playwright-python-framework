 Playwright Automation Framework - PROJECT PLAYWRIGHT PYTHON

A professional, data-driven automation framework built with Python, Playwright, and Pytest. This project demonstrates a scalable approach to web testing using external data sources and automated reporting.

🌟 Key Features:

Data-Driven Testing (DDT): Test cases are separated from logic using a test_data.csv file managed via Pandas.

Professional Reporting: Automated HTML reports with custom branding, titles, and execution summaries.

Visual Debugging: Automatic Screenshots and Video recordings on test failures.

Clean Architecture: Centralized configuration using pytest.ini and shared fixtures in conftest.py.

Environment Isolation: Managed via Python Virtual Environments (.venv) for consistency across machines.

🛠️ Tech Stack:

Language: Python 3.x
Library: Playwright (Python)
Test Runner: Pytest
Data Handling: Pandas & Openpyxl
Reports: Pytest-HTML

📁 Project Structure
Plaintext
├── tests/
│   └── test_data_driven_login_csv.py  # Core test logic
├── test_data.csv                      # External test data (User/Pass/Status)
├── conftest.py                        # Hooks for report branding & screenshots
├── pytest.ini                         # Global framework configuration
├── .gitignore                         # Prevents pushing junk files (venv, cache)
└── README.md                          # Project documentation


🚀 How to Run

Clone the Repo:
Bash
git clone <your-repo-link>

Activate Environment:
PowerShell
.\.venv\Scripts\activate

Run Tests & Generate Report:
PowerShell
pytest


📝 Lessons Learned (Troubleshooting):

During the development of this framework, several enterprise-level challenges were resolved:

Path Management: Implemented os.path logic to ensure data files are found regardless of execution directory.

Configuration Conflicts: Resolved duplicate name 'addopts' errors by merging CLI flags into a single, clean .ini structure.

Version Compatibility: Adapted pytest-html hooks to comply with v4.0+ "report object" requirements.