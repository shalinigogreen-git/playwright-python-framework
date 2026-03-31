🚀 **Playwright Automation Framework: PROJECT PLAYWRIGHT PYTHON**
A professional, Data-Driven Automation Framework built to showcase scalable web testing. This project separates test logic from test data, ensuring that the suite is maintainable and ready for enterprise-level deployments.

📌**Table of Contents**

🌟 Key Features
🛠️ Tech Stack
📁 Project Structure
🚀 How to Run:

📝 **Lessons Learned:**

🌟 Key Features
Data-Driven Testing (DDT): Test scenarios are fully decoupled from the code. All test cases are managed via an external test_data.csv file using the Pandas library.

Professional Reporting: Generates automated HTML Reports featuring custom company branding, dynamic titles, and detailed execution summaries.

Visual Debugging: Integrated Automatic Screenshots and Video Recordings that trigger specifically on test failures to speed up root-cause analysis.

Clean Architecture: Utilizes a centralized pytest.ini for global configuration and a conftest.py for shared fixtures and reporting hooks.

Environment Isolation: Built within a Python Virtual Environment (.venv) to ensure "it works on my machine" translates to "it works everywhere."

🛠️ **Tech Stack:**

Core Language: Python 3.x
Automation Tool: Playwright (Sync API)
Test Runner: Pytest
Data Processing: Pandas & Openpyxl
Reporting: Pytest-HTML (v4.0+)

**Project Structure**

Playwright_Python_Framework/
├── tests/
│   └── test_data_driven_login_csv.py  # Core test logic & parametrization
├── pages/                             # Future Page Object Model (POM) directory
├── test_results/                      # Automated storage for screenshots/videos
├── test_data.csv                      # External Data: (User, Pass, Expected Status)
├── conftest.py                        # Framework Hooks: Report branding & failures
├── pytest.ini                         # Global Config: Headed mode, CLI flags, logs
├── .gitignore                         # Security: Prevents pushing .venv and cache
└── README.md                          # Project Documentation

**How to Run:**
1. Clone the Repository:
git clone <your-repo-link>

2. Activate the Virtual Environment:
.\.venv\Scripts\activate

3. Execute the Suite:
pytest

(The framework will automatically read settings from pytest.ini and generate report.html)

📝 **Lessons Learned (Troubleshooting):**

Developing this framework provided deep insights into Enterprise Python Testing challenges:

* Dynamic Path Management: Solved directory issues by implementing os.path logic. This ensures the framework finds the test_data.csv whether it is run from the root or the sub-folder.

* Configuration Optimization: Resolved duplicate name 'addopts' conflicts by merging individual CLI flags into a single, optimized .ini structure.

* Library Versioning: Successfully migrated pytest-html hooks to comply with the new v4.0+ "Report Object" requirements, replacing outdated list-append methods with direct object attribute assignments.

* Idempotent Testing & Cleanup: Implemented logic to ensure tests are Idempotent (can be run 100 times with the same result). Managed browser contexts via Pytest Fixtures to ensure a clean state for every single row of data from the CSV, preventing "Session Leakage."

* Decoupled Configuration: Mastered the use of pytest.ini to separate "How the test runs" (Headed mode, Browser type) from "What the test does." This allows for seamless switching between Local Debugging and Headless CI/CD environments without touching the source code.

* Advanced Parameterization: Leveraged pytest.mark.parametrize with external data streams. Resolved complex data-type issues by implementing String Casting logic, ensuring that numeric data (like passwords "12345") from CSV/Excel is handled correctly by Playwright’s .fill() method.

* Failure Analysis & Traceability: Optimized the Failure Triage process. By configuring self-contained-html, I ensured that the entire test evidence package (logs, screenshots, and metadata) is portable and ready for immediate stakeholder review without external dependencies.

* Virtual Environment Portability: Resolved Fatal Launcher Errors caused by directory renaming. Developed a workflow for Dependency Management using pip freeze, ensuring that the Project Playwright Python framework remains reproducible across different developer machines.