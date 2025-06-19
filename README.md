# Frejun_Assignment

# 🧪 SauceDemo Selenium Automation Framework

This project is a complete **end-to-end Selenium automation framework** built using Python, Pytest, and the Page Object Model (POM).  
It automates user flows on [SauceDemo](https://www.saucedemo.com/), a demo e-commerce platform.

---

## ✅ Features

- ✅ Built using **Selenium**, **Pytest**, and **webdriver-manager**
- 🧱 Uses **Page Object Model (POM)** for better structure and reusability
- 💡 Covers both **positive** and **negative** scenarios
- 📄 Generates HTML test reports using `pytest-html`
- 🧪 Test scenarios covered:
  - Login
  - Sorting of items
  - Verify whether products are displayed
  - Add to cart and validate payment totals
  - Checkout process
  - Logout
  - Negative and edge-case login tests

---

## ⚙️ Setup Instructions

git clone https://github.com/ansarifawwad/Frejun_Assignment.git
cd Frejun_Assignment
python3 -m venv venv
source venv/bin/activate (for macOs)
pip3 install -r requirements.txt
pytest -v --html=report.html

