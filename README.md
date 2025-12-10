# Selenium Python Automation Mini Framework

This project is a **Selenium-based automation testing framework** built using the **Page Object Model (POM)** and **PyTest**.  
It demonstrates automation skills for QA roles, including structured test cases, browser automation, reusable page classes, and HTML reporting.

---

## 🚀 Features
- Selenium WebDriver automation (Chrome)
- Page Object Model (POM) structure
- PyTest test execution
- Auto WebDriver installation (webdriver-manager)
- HTML reports using pytest-html
- Reusable utility functions
- Organized folder structure

---

## 📁 Project Structure

Selenium-Automation-Framework/
│
├── tests/ # Test cases
│ ├── test_login.py
│ ├── test_search.py
│
├── pages/ # Page Object Model
│ ├── login_page.py
│ ├── search_page.py
│
├── utils/ # Helpers / driver setup
│ ├── driver_setup.py
│
├── reports/ # Test reports
│ ├── test_report.html
│
├── requirements.txt
├── README.md


---

## ▶️ How to Run Tests

### 1️⃣ Install dependencies


pip install -r requirements.txt


### 2️⃣ Run all tests


pytest tests/


### 3️⃣ Run tests with HTML report


pytest tests/ --html=reports/test_report.html


---

## 🧪 Sample Tests Included
- **Login Test** → Enter username, password, click login  
- **Google Search Test** → Perform search, validate title  

---

## 📌 Technologies Used
- Selenium (Python)
- PyTest
- WebDriver Manager
- Page Object Model (POM)
- HTML reporting (pytest-html)

---

## 📢 Purpose  
This project demonstrates:
- Ability to build automation frameworks  
- Use of Selenium WebDriver  
- Creating reusable page objects  
- Writing structured test cases  
- Generating HTML reports  
- Good coding + testing practices  

Perfect for **QA Engineer**, **Automation Engineer**, or **SDET** interviews.

---

## 👤 Author  
**Harsh Bansal**  
GitHub: https://github.com/harshbansal95623
