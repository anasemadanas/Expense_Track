# 💰 Money Manager App
> Organize your finances. Track your money. Plan smarter.

A modern and scalable financial management tool built in Python using a clean **3-Tier Architecture** and **SOLID principles**.


[![GitHub Repo](https://img.shields.io/badge/GitHub-Expense__Track-black?style=for-the-badge&logo=github)](https://github.com/anasemadanas/Expense_Track)
[![Last Commit](https://img.shields.io/github/last-commit/anasemadanas/Expense_Track?style=for-the-badge)](https://github.com/anasemadanas/Expense_Track)
[![Issues](https://img.shields.io/github/issues/anasemadanas/Expense_Track?style=for-the-badge)](https://github.com/anasemadanas/Expense_Track/issues)
[![Forks](https://img.shields.io/github/forks/anasemadanas/Expense_Track?style=for-the-badge)](https://github.com/anasemadanas/Expense_Track)
[![Stars](https://img.shields.io/github/stars/anasemadanas/Expense_Track?style=for-the-badge)](https://github.com/anasemadanas/Expense_Track)
[![License](https://img.shields.io/github/license/anasemadanas/Expense_Track?style=for-the-badge)](https://github.com/anasemadanas/Expense_Track)
[![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-Web%20Framework-green?style=for-the-badge&logo=django)](https://www.djangoproject.com/)

---

## 📑 Table of Contents

- [🧾 Introduction](#-introduction)
- [✨ Features](#-features)
- [🖼️ Screenshots](#️-screenshots)
- [📊 UML Diagrams](#-uml-diagrams)
- [🧱 Architecture](#-architecture)
- [📂 Project Structure](#-project-structure)
- [📦 Requirements](#-requirements)
- [⚙️ Installation](#️-installation)
- [▶️ Run the App](#️-run-the-app)
- [🙌 How to Contribute](#-how-to-contribute)
- [🔮 Future Enhancements](#-future-enhancements)
- [📝 License](#-license)
- [🔗 Contact](#-contact)

---

## 🧾 Introduction

**Money Manager** is a clean financial management application designed to help you:

- Track expenses and income
- Organize transactions into categories
- Plan monthly budgets
- View financial analytics through charts
- Take notes and set goals

Built using:

| Technology | Purpose |
|---|---|
| Python 3.10+ | Core language |
| PySide6 | GUI framework |
| SQLite | Local database |
| 3-Tier Architecture | Clean separation of concerns |
| Repository Pattern | Data access abstraction |
| SOLID Principles | Scalable & maintainable code |

---

## ✨ Features

- 📘 Track expenses & income
- 🏷️ Categorize transactions
- 📆 Monthly budget planning
- 📊 Dashboard with charts
- 🗒️ Notes & financial goals
- 🏛️ Clean and scalable architecture
- 🗄️ SQLite with Repository Pattern
- 🔌 Easy to extend or migrate (API / mobile / web)

---

## 🖼️ Screenshots

| Login | Dashboard | Transaction | Budget | Goal | ListTransaction |
|-------|-----------|-------------|--------|------|-----------------|
| ![Login](screenshots/Login.png) | ![Dashboard](screenshots/Dashboard.png) | ![Transaction](screenshots/transaction.png) | ![Budget](screenshots/budget.png) | ![Goal](screenshots/goal.png) | ![listTransaction](screenshots/listTransaction.png) |

---

## 📊 UML Diagrams

The diagram SVG files are stored in the [`screenshots/`](screenshots/) folder.

| Diagram | Preview | SVG Link |
|---|---|---|
| Use Case | <img src="screenshots/usecase.svg" width="300" alt="Use Case Diagram"/> | [Open SVG](screenshots/usecase.svg) |
| System ERD | <img src="screenshots/MoneyManagerERD.svg" width="300" alt="Money Manager ERD"/> | [Open SVG](screenshots/MoneyManagerERD.svg) |
| ERD | <img src="screenshots/erd.svg" width="300" alt="ERD"/> | [Open SVG](screenshots/erd.svg) |
| EER | <img src="screenshots/eer.svg" width="300" alt="EER"/> | [Open SVG](screenshots/eer.svg) |
| Dashboard ERD | <img src="screenshots/erd_dashboard.svg" width="300" alt="Dashboard ERD"/> | [Open SVG](screenshots/erd_dashboard.svg) |
| Login Sequence | <img src="screenshots/sequence_login.svg" width="300" alt="Login Sequence Diagram"/> | [Open SVG](screenshots/sequence_login.svg) |
| Add Budget Sequence | <img src="screenshots/sequence_add_budget.svg" width="300" alt="Add Budget Sequence Diagram"/> | [Open SVG](screenshots/sequence_add_budget.svg) |
| Add Transaction | <img src="screenshots/AddTransaction.svg" width="300" alt="Add Transaction Diagram"/> | [Open SVG](screenshots/AddTransaction.svg) |
| Edit Transaction Sequence | <img src="screenshots/sequence_edit_transaction.svg" width="300" alt="Edit Transaction Sequence Diagram"/> | [Open SVG](screenshots/sequence_edit_transaction.svg) |
| Dashboard Sequence | <img src="screenshots/sequence_dashboard.svg" width="300" alt="Dashboard Sequence Diagram"/> | [Open SVG](screenshots/sequence_dashboard.svg) |
| Object Snapshot | <img src="screenshots/object_add_transaction_snapshot.svg" width="300" alt="Add Transaction Object Snapshot"/> | [Open SVG](screenshots/object_add_transaction_snapshot.svg) |

---

## 🧱 Architecture

```
┌─────────────────────────────┐
│      Presentation Layer     │  ← PySide6 GUI / CLI
├─────────────────────────────┤
│    Business Logic Layer     │  ← Services, Validation, Calculations
├─────────────────────────────┤
│        Data Layer           │  ← SQLite + Repository Pattern + Interfaces
└─────────────────────────────┘
```

---

## 📂 Project Structure

```bash
Expense_Track 
├─.gitignore
├─.github    
├─LICENSE     
├─README.md
├─docs
├─money_manager
│ ├─__init__.py     
│ ├─main.py   
│ ├─resources_rc.py
| ├─common
│ ├─database
│ ├─models 
│ ├─repository   
│ ├─resources 
│ ├─services  
│ ├─tests 
│ └─ui 
└─screenshots  

```

---

## 📦 Requirements

```
Python 3.10+
PySide6
SQLite (included with Python)
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/anasemadanas/Expense_Track.git

# 2. Navigate to the project folder
cd Expense_Track/money_manager

# 3. Install requirements
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
python main.py
```

> Make sure you're inside the `money_manager/` folder before running.

---

## 🙌 How to Contribute

Pull Requests are welcome! Follow these steps:

1. **Fork** the repository
2. **Create** a feature branch → `git checkout -b feature/your-feature`
3. **Commit** your changes → `git commit -m "Add: your feature"`
4. **Push** to your branch → `git push origin feature/your-feature`
5. **Submit** a Pull Request

---

## 🔮 Future Enhancements

- 📱 Android version (Kivy / Flutter)
- 🌐 Web version (FastAPI + React)
- ☁️ Cloud sync
- 🧾 PDF reports
- 🤖 AI-powered spending predictions
- 🎨 Modern UI redesign

---

📊 Example Live Stats

![Repo Size](https://img.shields.io/github/repo-size/anasemadanas/Expense_Track?style=for-the-badge)

---

## 🌐 Live Demo

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Expense%20Track-green?style=for-the-badge&logo=django)](https://anasemad.pythonanywhere.com/)
![CI](https://img.shields.io/github/actions/workflow/status/anasemadanas/Expense_Track/django.yml?style=for-the-badge)

---

## 🔗 Contact

| Platform | Link |
|---|---|
| 🐙 GitHub | [GitHub](https://github.com/anasemadanas/) |
| 💼 LinkedIn | [LinkedIn](https://www.linkedin.com/in/eng-anasemad/) |
| 📧 Email | [Email](mailto:anaspython3@gmail.com) |

[↩️ Back to Table of Contents](#-table-of-contents)
