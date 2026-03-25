# 📄 Money Manager Project Documentation

**Version:** 1.0  
**Author:** Your Name  
**Language:** Python  
**Architecture:** 3-Tier + SOLID  
**Future Platforms:** Desktop, Android, Web

---

## 1️⃣ Introduction
**Project Name:** Money Manager App  
**Objective:** To manage expenses, income, budgets, notes, and financial goals efficiently.  
**Programming Language:** Python  
**Future Plans:** Android and Web versions  
**Architecture:** 3-Tier + SOLID principles

---

## 2️⃣ Project Objectives
- Track expenses and income  
- Categorize transactions  
- Manage monthly budgets  
- Dashboard with charts for financial reports  
- Notes & Goals system for reminders and objectives  
- Flexible architecture for future expansion (Android, Web)

---

## 3️⃣ System Architecture

### A. Presentation Layer (GUI Layer)
- Responsible for the graphical user interface (PyQt or Tkinter)  
- Does **not** contain business logic  
- Interacts only with the Business Layer

### B. Business Logic Layer (Service Layer)
- Contains all domain logic, calculations, and validations  
- Handles budget validation and transaction rules  
- Independent of UI and database

### C. Data Layer (Repository Layer)
- Responsible for data storage (SQLite, JSON, or API)  
- Contains Repositories and Interfaces  
- Allows changing the storage implementation without modifying the Business Layer

---

## 4️⃣ SOLID Principles
- **S (Single Responsibility):** Each class has one responsibility (e.g., `TransactionService`, `BudgetRepo`)  
- **O (Open/Closed):** Extend features without modifying existing classes  
- **L (Liskov Substitution):** Any repository can be replaced without breaking services  
- **I (Interface Segregation):** Small interfaces like `IBudgetRepo`, `ITransactionRepo`  
- **D (Dependency Inversion):** Upper layers depend on interfaces, not concrete classes

---

## 5️⃣ Features
- Expenses & Income Tracking  
- Budget Management  
- Notes & Goals system  
- Dashboard with charts  
- CRUD operations for all entities  
- Easy-to-use GUI

---

## 6️⃣ Folder Structure
```bash
Expense_Track/
│
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
│
└── money_manager/
    ├── __init__.py
    ├── main.py
    ├── src/
    │   ├── presentation/           # GUI Layer
    │   │   ├── __init__.py
    │   │   ├── views/
    │   │   │   ├── __init__.py
    │   │   │   ├── dashboard_view.py
    │   │   │   ├── add_transaction_view.py
    │   │   │   └── budget_view.py
    │   │   └── controllers/
    │   │       ├── __init__.py
    │   │       └── transaction_controller.py
    │   │
    │   ├── business/                # Service Layer
    │   │   ├── __init__.py
    │   │   ├── services/
    │   │   │   ├── __init__.py
    │   │   │   ├── transaction_service.py
    │   │   │   └── budget_service.py
    │   │   └── models/
    │   │       ├── __init__.py
    │   │       ├── transaction.py
    │   │       └── budget.py
    │   │
    │   ├── data/                    # Repository Layer
    │   │   ├── __init__.py
    │   │   ├── database.py
    │   │   ├── repositories/
    │   │   │   ├── __init__.py
    │   │   │   ├── transaction_repo.py
    │   │   │   └── budget_repo.py
    │   │   └── interfaces/
    │   │       ├── __init__.py
    │   │       ├── ITransactionRepo.py
    │   │       └── IBudgetRepo.py
    │   │
    │   └── shared/
    │       ├── __init__.py
    │       ├── util.py
    │       └── constants.py
    │
    └── tests/
        ├── __init__.py
        ├── test_transaction_service.py
        ├── test_budget_service.py
        └── test_repo.py
```
---

## 7️⃣ Database Design
- **Budget Table:** id, name, amount  
- **Transaction Table:** id, name, amount, category, date  
- **Notes Table:** id, title, content, date, tag  

---

## 8️⃣ Future Enhancements
- Android app (Kivy or Flutter)  
- Web app (FastAPI + React)  
- Cloud sync (Firebase/Supabase)  
- PDF/Excel Reports  
- AI-based suggestions for spending and saving

---

## 9️⃣ How to Run
1. Clone the repository:  
```bash
git clone https://github.com/anasemadanas/Expense_Track.git
cd Expense_Track
pip install -r requirements.txt
python money_manager/main.py
