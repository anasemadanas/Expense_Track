# 💰 Money Manager App

> A Python desktop application for managing personal finances — track expenses, income, budgets, notes, and financial goals efficiently.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://python.org)
[![Architecture](https://img.shields.io/badge/Architecture-3--Tier-blue)](https://en.wikipedia.org/wiki/Multitier_architecture)
[![SOLID](https://img.shields.io/badge/Design-SOLID%20Principles-green)](https://en.wikipedia.org/wiki/SOLID)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-In%20Development-orange)]()

**Version:** 1.0  
**Author:** Team Student
**Language:** Python  
**Architecture:** 3-Tier + SOLID  
**Future Platforms:** Desktop, Android, Web

---

## 📋 Table of Contents

- [Introduction](#-introduction)
- [Project Objectives](#-project-objectives)
- [Features](#-features)
- [System Architecture](#-system-architecture)
- [SOLID Principles](#-solid-principles)
- [Folder Structure](#-folder-structure)
- [Database Design](#-database-design)
- [Functional Requirements](#-functional-requirements)
- [Non-Functional Requirements](#-non-functional-requirements)
- [How to Run](#-how-to-run)
- [Future Enhancements](#-future-enhancements)
- [Constraints & Assumptions](#-constraints--assumptions)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🧭 Introduction

**Project Name:** Money Manager App  
**Objective:** To manage expenses, income, budgets, notes, and financial goals efficiently.  
**Programming Language:** Python  
**Future Plans:** Android and Web versions  
**Architecture:** 3-Tier + SOLID principles

The Money Manager Application is a standalone desktop personal finance tool that enables individuals to track income and expenses, categorize transactions, manage monthly budgets, set personal financial goals, write notes, and view visual reports from an intuitive desktop GUI. The system is built in Python using a strict 3-Tier + SOLID architecture to ensure maintainability and future extensibility to Android and Web platforms.

---

## 🎯 Project Objectives

- Track expenses and income
- Categorize transactions
- Manage monthly budgets
- Dashboard with charts for financial reports
- Notes & Goals system for reminders and objectives
- Flexible architecture for future expansion (Android, Web)

---

## ✨ Features

| Feature | Description |
|---|---|
| **Expenses & Income Tracking** | Record, edit, and delete financial transactions with categorization |
| **Budget Management** | Define per-category monthly budgets with over-limit alerting |
| **Notes & Goals System** | Attach notes to entries and track progress toward savings goals |
| **Dashboard with Charts** | Visual summary of financial health with trend lines and pie charts |
| **CRUD Operations** | Full create/read/update/delete for all entities |
| **Reports Export** | Generate PDF and Excel reports filtered by date or category |
| **Multi-currency Support** | User-configurable display currency |
| **Easy-to-use GUI** | Built with PySide6  |

---

## 🏗 System Architecture

The application follows a strict **3-Tier Architecture**, enforcing clear separation of concerns. Each tier communicates exclusively with the adjacent tier through well-defined interfaces.

```
┌─────────────────────────────────────────────────┐
│          PRESENTATION LAYER (GUI)               │
│      PySide6 • Views • Event Handlers           │
└──────────────────────┬──────────────────────────┘
                       │ calls
┌──────────────────────▼──────────────────────────┐
│       BUSINESS LOGIC LAYER (Service)            │
│ TransactionService • BudgetService • Validators │
│           UserService • DashboardService        │
└──────────────────────┬──────────────────────────┘
                       │ calls
┌──────────────────────▼──────────────────────────┐
│           DATA LAYER (Repository)               │
│   IUserRepo • ITransactionRepo • IBudgetRepo    │
│                                                 │
└──────────────────────┬──────────────────────────┘
                       │
                  [ SQLite DB ]
```

### A. Presentation Layer (GUI Layer)

- Responsible for the graphical user interface (PySide6)
- Does **not** contain business logic
- Interacts only with the Business Layer

### B. Business Logic Layer (Service Layer)

- Contains all domain logic, calculations, and validations
- Handles budget validation and transaction rules
- Independent of UI and database

### C. Data Layer (Repository Layer)

- Responsible for data storage (SQLite)
- Contains Repositories and Interfaces
- Allows changing the storage implementation without modifying the Business Layer

---

## 🧱 SOLID Principles

All components are designed in strict adherence to SOLID principles:

| Principle | Application |
|---|---|
| **S — Single Responsibility** | Each class has one responsibility (e.g., `TransactionService`, `BudgetRepo`) |
| **O — Open/Closed** | Extend features without modifying existing classes |
| **L — Liskov Substitution** | Any repository can be replaced without breaking services |
| **I — Interface Segregation** | Small interfaces like `IBudgetRepo`, `ITransactionRepo` |
| **D — Dependency Inversion** | Upper layers depend on interfaces, not concrete classes |

---

## 📁 Folder Structure

```
Expense_Track                 
├─.gitignore                  
├─LICENSE                     
├─README.md                   
└─money_manager               
  ├─__init__.py               
  ├─main.exe                  
  ├─main.py                   
  ├─main.spec                 
  ├─requirements.txt          
  ├─Resources_rc.py           
  ├─data                      
  │ ├─__init__.py             
  │ ├─app_state.py            
  │ ├─database.py             
  │ ├─interfaces              
  │ │ ├─__init__.py           
  │ │ ├─IBudgetRepo.py        
  │ │ ├─IGoalRepo.py          
  │ │ ├─ITransactionRepo.py   
  │ │ └─IUserRepo.py          
  │ └─repositories            
  │   ├─__init__.py           
  │   ├─budget_repo.py        
  │   ├─goal_repo.py          
  │   ├─transaction_repo.py   
  │   └─user_repo.py          
  ├─Database                  
  │ └─Money_Manager_DB.db     
  ├─Services                  
  │ ├─__init__.py             
  │ ├─budget_service.py       
  │ ├─dashboard_service.py    
  │ ├─goal_service.py         
  │ ├─transaction_service.py  
  │ ├─user_service.py         
  │ └─models                  
  │   ├─__init__.py           
  │   ├─budget.py             
  │   ├─goal.py               
  │   ├─permissions.py        
  │   ├─transaction.py        
  │   └─user.py               
  └─ui                        
    ├─__init__.py             
    ├─frmAddBudget.py         
    ├─frmAddTransaction.py    
    ├─frmdashboard.py         
    ├─frmGoals.py             
    ├─frmListTransaction.py   
    ├─frmLoginScreen.py       
    ├─ui_frmAddBudget.py      
    ├─ui_frmAddTransaction.py 
    ├─ui_frmdashboard.py      
    ├─ui_frmGoals.py          
    ├─ui_frmListTransaction.py
    └─ui_frmLogin.py          

         
```

---

## 🗃 Database Design

The application uses **SQLite** for local data persistence. All entities are linked to the `User` entity, enforcing data isolation per user account.

### Entity-Relationship Overview

```
┌──────────┐       ┌──────────────┐
│   User   │──1:N──│ Transaction  │
│          │       └──────────────┘
│  id (PK) │       ┌──────────────┐
│ username │──1:N──│    Budget    │
│ password │       └──────────────┘
│          │       ┌──────────────┐
│          │──1:N──│    Goals     │
└──────────┘       └──────────────┘
```

### Tables

**`users`** — `id`, `username`, `password`, `Permissions`

**`transactions`** — `id`, `amount`, `category`, `month`, `Year`

**`budgets`** — `id`,  `amount`, `month`, `Year`, `Total_amount`

**`Goals`** — `id`, `name`  `target_amount`, `saved_amount`

---

## 📌 Functional Requirements

### FR-01: Transaction Management
- Add new transactions with name, amount, category, and date
- View all transactions with filtering by date range, category, and type
- Edit any field of an existing transaction
- Delete a transaction with confirmation prompt
- Auto-categorize transactions based on configurable keyword rules

### FR-02: Budget Management
- Define a monthly budget per category with a monetary cap
- Display current spending vs budget limit in real time
- Trigger visual alert when spending reaches 80% of a budget limit
- Full CRUD on budget entries

### FR-03: Dashboard & Reports
- Display total income, total expenses, and net balance for the current month
- Pie chart of spending by category
- Bar/line chart showing monthly spending trends
- Export financial reports to PDF or Excel format

### FR-04: Notes & Goals
- Create notes with title, content, date, and optional tags
- Define savings goals with target amount and deadline
- Calculate and display percentage completion of each goal
- In-app reminders for approaching goal deadlines

---

## ⚙️ Non-Functional Requirements

| ID | Category | Requirement |
|---|---|---|
| NFR-01 | **Performance** | Launch in under 3 seconds; GUI responses under 200ms |
| NFR-02 | **Reliability** | No data loss or corruption; atomic writes via DB transactions |
| NFR-03 | **Usability** | Core tasks completable within 5 minutes without documentation |
| NFR-04 | **Security** | Passwords hashed with bcrypt; no plaintext credentials |
| NFR-05 | **Maintainability** | Unit test coverage > 80%; docstrings on all public methods |
| NFR-06 | **Portability** | Runs on Windows 10+, macOS 12+, Ubuntu 20.04+ |
| NFR-07 | **Scalability** | Repository layer swappable with zero service-layer changes |
| NFR-08 | **Data Integrity** | Foreign key constraints enforced; cascading deletes configured |

---

## 📌 Prerequisites

Before you start, make sure you have:

* Python 3.10 or higher
* pip (Python package manager)

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/anasemadanas/Expense_Track.git
cd Expense_Track
```

---

### 2. Create Virtual Environment & Install Dependencies

```bash
python -m venv .venv
```

#### Activate the environment:

* On Windows:

```bash
.venv\Scripts\activate
```

* On macOS/Linux:

```bash
source .venv/bin/activate
```

#### Install dependencies:

```bash
pip install -r requirements.txt
```

---

### 3. Run the Application

```bash
python money_manager/main.py
```

> ⚠️ Make sure you're in the root project folder (`Expense_Track`)

---

## 🧪 Testing & Development

### Install Dev Dependencies

```bash
pip install -r requirements-dev.txt
```

---

### Run Tests

```bash
pytest
```

---

## 📦 Build Executable

```bash
pyinstaller --onefile --noconsole money_manager/main.py
```

> 📌 The executable will be generated inside the `dist/` folder.

---

## 🎬 Preview

![App Screenshot](https://raw.githubusercontent.com/anasemadanas/Expense_Track/main/screenshots/Dashboard.png)

---

## 🧰 Features

* Add expenses
* Track income
* Simple and clean UI
* Local data storage




---

## 🔮 Future Enhancements

| Enhancement | Details |
|---|---|
| **Android App** | Kivy or Flutter with shared Python backend |
| **Web App** | FastAPI + React |
| **Cloud Sync** | Firebase / Supabase |
| **PDF/Excel Reports** | Scheduled report generation with embedded charts |
| **AI-based Insights** | Automatic transaction classification and spending suggestions |
| **Multi-User / Family Mode** | Role-based access (admin/viewer) for household budgets |

---

## 🔒 Constraints & Assumptions

### Constraints
- v1.0 supports a single local user; multi-user deferred to v2.0
- GUI built with Python-native libraries (PyQt5 or Tkinter) only
- Data stored locally in SQLite; cloud backup is optional
- No internet connectivity required for core functionality
- Distributed as a self-contained executable via PyInstaller

### Assumptions
- Users have basic familiarity with personal finance concepts
- Development environment uses Python 3.10+ with pip
- SQLite bundled with Python is sufficient for single-user workload
- Monetary values stored as REAL with 2-decimal precision at the application layer
- Dates stored as ISO 8601 strings (YYYY-MM-DD)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure your code follows the SOLID principles and the 3-Tier architecture outlined above.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](https://github.com/anasemadanas/Expense_Track/blob/main/LICENSE) file for details.

---
[↩️ Back to Table of Contents](#-Table-of-Contents)
---
<p align="center">
  <sub>Built with ❤️ using Python • Designed with SOLID principles in mind</sub>
</p>
