# 💰 Money Manager Web Application

> A full-stack personal finance management system built with Django, following 3-Tier Architecture, SOLID principles, and clean scalable design.

---

# 📌 Project Overview

Project Name: Money Manager Web App  
Type: Web Application (Django)  
Backend: Django 6+  
Database: SQLite (dev) → PostgreSQL (future)  
Architecture: 3-Tier + Clean Architecture  
Status: In Development  
Author: Team Student  

---

# 🎯 Objective

This system helps users manage personal finances:

- Track income and expenses
- Category-based transactions
- Budget management
- Financial goals tracking
- Dashboard analytics

Designed for future scaling:
- REST API
- Mobile apps
- Cloud multi-user system

---

# ✨ Features

## 👤 Authentication
- Login / Logout
- Django session authentication
- Admin panel

## 💰 Transactions
- Income & expenses
- Categories
- CRUD operations
- Monthly filtering

## 📊 Dashboard
- Total income
- Total expenses
- Net balance
- Budget overview
- Goals progress

## 🎯 Goals
- Savings goals
- Progress tracking
- Completion status

## 💳 Budget
- Monthly category budgets
- Spending tracking

---

# 🏗 Architecture

Presentation Layer (UI)
↓
Business Logic Layer (services/)
↓
Data Layer (repository/)
↓
SQLite Database

---

# 📁 Project Structure

```text
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
├── expenses/
│   ├── views.py
│   ├── models.py
│   ├── admin.py
│
├── services/
│   ├── user_service.py
│   ├── dashboard_service.py
│   ├── transaction_service.py
│   ├── budget_service.py
│   └── goal_service.py
│
├── repository/
│   ├── user_repo.py
│   ├── transaction_repo.py
│   ├── budget_repo.py
│   └── goal_repo.py
│
├── models/
│   ├── user.py
│   ├── transaction.py
│   ├── budget.py
│   └── goal.py
│
├── common/
│   ├── utils.py
│   └── activity_logger.py
│
├── templates/
│   ├── login.html
│   └── dashboard.html
│
├── database/
│   ├── schema.sql
│   └── database.py
│
└── resources/
    └── icons/

```

# ⚙️ Money Manager Web - Setup Guide

## 1. 📥 Clone Project

```bash
git clone https://github.com/your-repo/Expense_Track.git
cd Expense_Track/money_manager_web
```

## ⚙️ Setup Guide

### 1. 📥 Clone Project
```bash
git clone https://github.com/your-repo/Expense_Track.git
cd Expense_Track/money_manager_web
```

### 2. 🐍 Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

### 3. 📦 Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. 🗄️ Run Migrations
```bash
python manage.py migrate
```

### 5. 👤 Create Admin User
```bash
python manage.py createsuperuser
```

Example:
```text
username: admin
password: 1234
```

### 6. 🚀 Run Server
```bash
python manage.py runserver
```

---

### 🌐 Access Application
```text
http://127.0.0.1:8000/login/
```

---

### 🔐 Test Login
```text
username: admin
password: 1234
```

---

### ⚠️ Common Errors & Fixes

❌ no such table: auth_user
```bash
python manage.py migrate
```

❌ no such table: django_session
```bash
python manage.py migrate
```

---

### 🚀 Future Improvements
- REST API (Django REST Framework)
- JWT Authentication
- Mobile App Integration
- AI Spending Analysis
- PostgreSQL Migration
- Real-time Updates
```
