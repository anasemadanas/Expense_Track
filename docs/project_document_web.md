# 💰 Money Manager Web Application

> A full-stack personal finance management system built with Django, following **3-Tier Architecture**, **SOLID principles**, and scalable clean architecture design.

---

## 📌 Project Overview

**Project Name:** Money Manager Web App  
**Type:** Web Application (Django)  
**Backend:** Django 6+  
**Database:** SQLite (development) → PostgreSQL (future)  
**Architecture:** 3-Tier + Clean Architecture Principles  
**Status:** In Development  
**Author:** Team Student  

---

## 🎯 Objective

The goal of this system is to provide a **simple yet powerful financial management platform** that allows users to:

- Track income and expenses
- Manage budgets per category
- Set financial goals
- View dashboard analytics
- Store and retrieve financial history securely

The system is designed to be **scalable**, allowing future expansion into:
- Mobile App (Flutter / Kivy)
- REST API backend
- Cloud-based multi-user system

---

## ✨ Features

### 👤 Authentication
- Login / Logout system
- Session-based authentication (temporary testing mode)
- Future: Django auth + JWT support

### 💰 Transactions
- Add income and expenses
- Categorization (Food, Salary, etc.)
- Monthly filtering
- CRUD operations

### 📊 Dashboard
- Total income
- Total expenses
- Net balance
- Budget summary
- Goals progress
- Transaction overview

### 🎯 Goals System
- Create savings goals
- Track progress percentage
- Completion tracking

### 💳 Budget System
- Monthly budgets per category
- Spending tracking
- Limit alerts (future enhancement)

---

## 🏗 System Architecture (3-Tier)

```text id="arch_01"
┌──────────────────────────────┐
│   Presentation Layer (UI)    │
│   Django Templates / Views   │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ Business Logic Layer         │
│ services/                    │
│ - user_service               │
│ - dashboard_service          │
│ - transaction_service        │
│ - budget_service             │
│ - goal_service               │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ Data Access Layer            │
│ repository/                  │
│ - user_repo                 │
│ - transaction_repo          │
│ - budget_repo               │
│ - goal_repo                 │
└──────────────┬───────────────┘
               │
               ▼
        SQLite Database
📁 Project Structure
money_manager_web/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── expenses/                 # Main app (views layer)
│   ├── views.py
│   ├── models.py
│   ├── admin.py
│
├── services/                 # Business logic layer
│   ├── user_service.py
│   ├── dashboard_service.py
│   ├── transaction_service.py
│   ├── budget_service.py
│   ├── goal_service.py
│
├── repository/               # Data access layer
│   ├── user_repo.py
│   ├── transaction_repo.py
│   ├── budget_repo.py
│   ├── goal_repo.py
│
├── models/                   # Domain models
│   ├── user.py
│   ├── transaction.py
│   ├── budget.py
│   ├── goal.py
│
├── common/                   # Utilities
│   ├── utils.py
│   ├── activity_logger.py
│
├── templates/
│   ├── login.html
│   ├── dashboard.html
│
├── database/
│   ├── schema.sql
│   ├── database.py
│
└── resources/
    ├── icons/
⚙️ Installation & Setup
1️⃣ Clone Project
git clone https://github.com/your-repo/Expense_Track.git
cd Expense_Track/money_manager_web
2️⃣ Create Virtual Environment
python -m venv .venv

Activate:

.venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Database Migrations
python manage.py migrate
5️⃣ Create Admin User (Optional)
python manage.py createsuperuser

Example:

username: admin
password: 1234
6️⃣ Run Server
python manage.py runserver
🌐 Access Application
http://127.0.0.1:8000/login/
🔐 Login Credentials (Testing Mode)
username: admin
password: 1234
⚠️ Common Issues
❌ Error: no such table: auth_user
python manage.py migrate
❌ Login not working
Ensure migrations are applied
Check session middleware enabled
Verify views logic
🚀 Future Enhancements
- REST API (Django REST Framework)
- JWT Authentication
- Mobile App (Flutter)
- AI Spending Analysis
- Cloud Sync (PostgreSQL)
- Multi-user system
- Real-time notifications
- Charts (Chart.js)
🧠 Architecture Principles

This project strictly follows:

✔ Single Responsibility Principle
✔ Open/Closed Principle
✔ Liskov Substitution Principle
✔ Interface Segregation Principle
✔ Dependency Inversion Principle
📊 Database Design
User
 ├── Transactions (1:M)
 ├── Budgets (1:M)
 └── Goals (1:M)
🤝 Contribution Guide
1. Fork repository
2. Create feature branch
3. Commit changes
4. Push branch
5. Open Pull Request
📄 License
MIT License
❤️ Author Note

This project is built for learning real-world software architecture, not just CRUD.

Focus areas:

Clean architecture
Separation of concerns
Scalable backend design