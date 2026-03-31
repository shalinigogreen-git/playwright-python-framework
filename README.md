# 🚀 Playwright Python Automation Framework

A scalable and production-ready UI automation framework built using **Playwright + Pytest**, designed for reliable end-to-end testing with CI/CD integration.

---

## 📌 Project Overview

This project demonstrates a modern automation framework using:
- Playwright for browser automation
- Pytest for test execution and structure
- Page Object Model (POM) for maintainability
- CI/CD using GitHub Actions
- Screenshot & video capture for debugging failures

---

## 🛠️ Tech Stack

- Python 🐍
- Playwright 🎭
- Pytest ⚙️
- GitHub Actions 🚀

---

## 📁 Project Structure
project/
│
├── tests/ # Test cases
├── pages/ # Page Object Model classes
├── screenshots/ # Failure screenshots
├── videos/ # Test execution videos
│
├── conftest.py # Fixtures & hooks
├── pytest.ini # Pytest config
├── requirements.txt # Dependencies
└── .github/workflows/ # CI/CD pipeline


---

## ⚙️ Setup Instructions

### 1. Clone the repository

git clone git@github.com
:your-username/playwright-framework.git
cd playwright-framework


### 2. Install dependencies

pip install -r requirements.txt


### 3. Install Playwright browsers

playwright install


---

## ▶️ Run Tests


pytest


Run with browser UI:

pytest --headed


---

## 📸 Features

✅ Page Object Model (POM)  
✅ Pytest fixtures & parametrization  
✅ Screenshot capture on failure  
✅ Video recording of test execution  
✅ HTML reporting  
✅ CI/CD with GitHub Actions  

---

## 📊 Reports

Generate HTML report:

pytest --html=report.html

---

## 🔄 CI/CD Integration

- Tests run automatically on every push
- Reports, screenshots, and videos are uploaded as artifacts

📍 Check GitHub Actions tab for execution details

---

## 🧠 Key Highlights

- Scalable automation framework design  