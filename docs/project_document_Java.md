# 💰 Money Manager App — Java Edition

> A Java desktop application for managing personal finances — track expenses, income, budgets, notes, and financial goals efficiently.

[![Java](https://img.shields.io/badge/Java-17%20LTS-007396?logo=openjdk&logoColor=white)](https://openjdk.org)
[![Maven](https://img.shields.io/badge/Build-Apache%20Maven%203.9%2B-C71A36?logo=apachemaven&logoColor=white)](https://maven.apache.org)
[![JavaFX](https://img.shields.io/badge/UI-JavaFX%2021-1F7A8C?logo=openjdk&logoColor=white)](https://openjfx.io)
[![PostgreSQL](https://img.shields.io/badge/DB-PostgreSQL%2016-4169E1?logo=postgresql&logoColor=white)](https://postgresql.org)
[![Architecture](https://img.shields.io/badge/Architecture-3--Tier-blue)](https://en.wikipedia.org/wiki/Multitier_architecture)
[![SOLID](https://img.shields.io/badge/Design-SOLID%20Principles-green)](https://en.wikipedia.org/wiki/SOLID)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-In%20Development-orange)]()

**Version:** 1.0
**Author:** Team Student
**Language:** Java 17 LTS
**Build System:** Apache Maven 3.9+
**UI Framework:** JavaFX 21
**Database:** PostgreSQL 16
**Architecture:** 3-Tier + SOLID
**Future Platforms:** Desktop, Android, Web

---

## 📋 Table of Contents

- [Introduction](#-introduction)
- [Project Objectives](#-project-objectives)
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [System Architecture](#-system-architecture)
- [SOLID Principles](#-solid-principles)
- [Folder Structure](#-folder-structure)
- [Database Design](#-database-design)
- [Functional Requirements](#-functional-requirements)
- [Non-Functional Requirements](#-non-functional-requirements)
- [Maven Build & Run](#-maven-build--run)
- [Testing](#-testing)
- [Future Enhancements](#-future-enhancements)
- [Constraints & Assumptions](#-constraints--assumptions)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🧭 Introduction

**Project Name:** Money Manager App — Java Edition
**Objective:** To manage expenses, income, budgets, notes, and financial goals efficiently.
**Programming Language:** Java 17 LTS
**Build System:** Apache Maven 3.9+
**Database:** PostgreSQL 16
**UI:** JavaFX 21 (FXML + CSS)
**Future Plans:** Android (Kotlin/Jetpack Compose) and Web (Spring Boot + React) versions
**Architecture:** 3-Tier + SOLID principles

The Money Manager Application (Java Edition) is a standalone desktop personal-finance tool that enables individuals to track income and expenses, categorize transactions, manage monthly budgets, set personal financial goals, write notes, and view visual reports from an intuitive JavaFX desktop GUI. The system is built in Java using a strict 3-Tier + SOLID architecture backed by PostgreSQL to ensure transactional integrity, maintainability, and future extensibility to Android and Web platforms.

---

## 🎯 Project Objectives

- Track expenses and income with full CRUD operations
- Categorize transactions (income / expense)
- Manage monthly per-category budgets with real-time over-limit alerts
- Present a dashboard with charts for financial reports
- Notes & Goals system for reminders and savings targets
- Flexible architecture for future expansion (Android, Web, Cloud sync)
- Transactional safety via PostgreSQL ACID guarantees

---

## ✨ Features

| Feature | Description |
|---|---|
| **Expenses & Income Tracking** | Record, edit, and delete financial transactions with categorization |
| **Budget Management** | Define per-category monthly budgets with over-limit alerting |
| **Notes & Goals System** | Attach notes to entries and track progress toward savings goals |
| **Dashboard with Charts** | Visual summary of financial health via JavaFX PieChart & LineChart |
| **CRUD Operations** | Full create/read/update/delete for all entities |
| **Reports Export** | Generate PDF (iText) and Excel (Apache POI) reports filtered by date or category |
| **Multi-currency Support** | User-configurable ISO-4217 display currency |
| **Easy-to-use GUI** | Built with JavaFX 21 (FXML markup + CSS styling) |
| **Internationalization** | Strings externalised via `ResourceBundle` .properties files |

---

## 🧰 Technology Stack

| Layer | Technology | Notes |
|---|---|---|
| Language | Java 17 LTS | Source/target bytecode 17 |
| Build / Deps | Apache Maven 3.9+ | POM-driven, reproducible builds |
| UI | JavaFX 21 (FXML + CSS) | OpenJFX via Maven |
| Dependency Injection | Spring Framework 6 (optional) | Constructor injection preferred |
| Data Access | Spring Data JPA + Hibernate 6 | JPA 3.1 (Jakarta) |
| Database | PostgreSQL 16 | JDBC driver `org.postgresql:postgresql` |
| Connection Pool | HikariCP | Default Spring Boot pool |
| Schema Migrations | Flyway | Runs on startup |
| Password Hashing | Spring Security Crypto (BCrypt) | No plaintext storage |
| PDF Export | iText 7 / OpenPDF | Financial reports |
| Excel Export | Apache POI | XLSX reports |
| Logging | SLF4J + Logback | Rolling file + console appenders |
| Testing | JUnit 5, Mockito, AssertJ, Testcontainers | Disposable PostgreSQL in integration tests |
| Coverage | JaCoCo | Enforce ≥ 80 % in pom.xml |
| Packaging | maven-shade-plugin / jpackage | Fat JAR and native installers |

---

## 🏗 System Architecture

The application follows a strict **3-Tier Architecture**, enforcing clear separation of concerns. Each tier communicates exclusively with the adjacent tier through well-defined Java interfaces.

```
┌─────────────────────────────────────────────────┐
│          PRESENTATION LAYER (GUI)               │
│     JavaFX • FXML Views • Controllers • CSS     │
└──────────────────────┬──────────────────────────┘
                       │ calls
┌──────────────────────▼──────────────────────────┐
│       BUSINESS LOGIC LAYER (Service)            │
│ TransactionService • BudgetService • Validators │
│        UserService • DashboardService           │
└──────────────────────┬──────────────────────────┘
                       │ calls
┌──────────────────────▼──────────────────────────┐
│           DATA LAYER (Repository / JPA)         │
│   IUserRepo • ITransactionRepo • IBudgetRepo    │
│ JpaUserRepo • JpaTransactionRepo • JpaBudgetRepo│
└──────────────────────┬──────────────────────────┘
                       │ JDBC (HikariCP)
                 [ PostgreSQL 16 ]
```

### A. Presentation Layer (GUI Layer)

- Responsible for the graphical user interface (JavaFX 21)
- FXML markup + CSS theming + Java Controllers
- Does **not** contain business logic
- Interacts only with the Business Layer via DTOs

### B. Business Logic Layer (Service Layer)

- Contains all domain logic, calculations, and validations
- Handles budget validation and transaction rules
- Independent of UI and database
- Depends only on repository interfaces

### C. Data Layer (Repository / JPA Layer)

- Responsible for data storage (PostgreSQL via JPA/Hibernate)
- Contains Repositories and Interfaces
- Flyway manages schema migrations
- Allows changing the storage implementation (e.g. REST client) without modifying the Business Layer

---

## 🧱 SOLID Principles

All components are designed in strict adherence to SOLID principles:

| Principle | Application |
|---|---|
| **S — Single Responsibility** | Each class has one responsibility (e.g., `TransactionService`, `JpaBudgetRepo`) |
| **O — Open/Closed** | Extend features (new report types, new storage backends) without modifying existing classes |
| **L — Liskov Substitution** | Any repository (`JpaTransactionRepo`, `RestTransactionRepo`) can be swapped without breaking services |
| **I — Interface Segregation** | Small focused interfaces like `IBudgetRepo`, `ITransactionRepo`, `IGoalRepo` |
| **D — Dependency Inversion** | Services depend on interfaces, dependencies injected via Spring or constructor DI — easy Mockito mocking in tests |

---

## 📁 Folder Structure

```
money-manager/
├── pom.xml
├── src/main/java/com/teamstudent/moneymanager/
│   ├── MoneyManagerApp.java           # JavaFX Application entry point
│   ├── config/                        # AppConfig, DataSourceConfig, BeanConfig
│   ├── ui/
│   │   ├── controller/                # LoginController, DashboardController,
│   │   │                               #   TransactionController, BudgetController
│   │   └── FxmlLoaderFactory.java
│   ├── service/
│   │   ├── TransactionService.java
│   │   ├── BudgetService.java
│   │   ├── GoalService.java
│   │   ├── DashboardService.java
│   │   └── UserService.java
│   ├── repository/
│   │   ├── IUserRepo.java
│   │   ├── ITransactionRepo.java
│   │   ├── IBudgetRepo.java
│   │   ├── IGoalRepo.java
│   │   └── jpa/                       # JpaUserRepo, JpaTransactionRepo …
│   ├── model/                         # @Entity classes: User, Transaction, Budget, Goal
│   ├── dto/                           # Data-transfer objects
│   └── util/                          # Validators, Currency/Date formatters
├── src/main/resources/
│   ├── fxml/                          # login.fxml, dashboard.fxml, transaction.fxml …
│   ├── css/                           # application.css
│   ├── i18n/                          # messages_en.properties, messages_ar.properties …
│   ├── db/migration/
│   │   ├── V1__init.sql               # Flyway migration
│   │   └── V2__indexes.sql
│   ├── application.yml
│   └── logback.xml
└── src/test/java/com/teamstudent/moneymanager/
    ├── service/                       # Service unit tests (JUnit 5 + Mockito)
    └── repository/                    # Integration tests (Testcontainers PostgreSQL)
```

---

## 🗃 Database Design

The application uses **PostgreSQL 16** for relational persistence. Schema migrations are managed by **Flyway** on application startup. All entities are linked to the `users` entity via foreign keys with `ON DELETE CASCADE`.

### Entity-Relationship Overview

```
┌──────────────┐       ┌───────────────────┐
│    users     │──1:N──│   transactions    │
│              │       └───────────────────┘
│ user_id PK   │       ┌───────────────────┐
│ username     │──1:N──│     budgets       │
│ password_hash│       └───────────────────┘
│ created_at   │       ┌───────────────────┐
│              │──1:N──│      goals        │
└──────────────┘       └───────────────────┘
```

### Tables

**`users`**

| Column | Type | Constraints |
|---|---|---|
| user_id | `BIGSERIAL` | PRIMARY KEY |
| username | `VARCHAR(50)` | NOT NULL UNIQUE |
| password_hash | `TEXT` | NOT NULL (BCrypt) |
| created_at | `TIMESTAMPTZ` | NOT NULL DEFAULT now() |

**`transactions`**

| Column | Type | Constraints |
|---|---|---|
| transaction_id | `BIGSERIAL` | PRIMARY KEY |
| user_id | `BIGINT` | NOT NULL REFERENCES users(user_id) ON DELETE CASCADE |
| name | `VARCHAR(100)` | NOT NULL |
| amount | `NUMERIC(12,2)` | NOT NULL CHECK (amount > 0) |
| category | `VARCHAR(50)` | NOT NULL |
| tx_type | `VARCHAR(10)` | NOT NULL CHECK (tx_type IN ('INCOME','EXPENSE')) |
| tx_date | `DATE` | NOT NULL |
| created_at | `TIMESTAMPTZ` | NOT NULL DEFAULT now() |

**`budgets`**

| Column | Type | Constraints |
|---|---|---|
| budget_id | `BIGSERIAL` | PRIMARY KEY |
| user_id | `BIGINT` | NOT NULL REFERENCES users(user_id) ON DELETE CASCADE |
| category | `VARCHAR(50)` | NOT NULL |
| amount_cap | `NUMERIC(12,2)` | NOT NULL CHECK (amount_cap > 0) |
| month | `SMALLINT` | NOT NULL CHECK (month BETWEEN 1 AND 12) |
| year | `SMALLINT` | NOT NULL CHECK (year >= 2020) |
| — | `UNIQUE` | (user_id, category, month, year) |

### Indexes

- `idx_tx_user_date` — btree on `(user_id, tx_date DESC)` — accelerates recent-transaction queries
- `idx_tx_user_cat`  — btree on `(user_id, category)` — accelerates per-category reports
- `idx_bg_user_ym`   — btree on `(user_id, year, month)` — accelerates monthly budget lookup

---

## 📌 Functional Requirements

### FR-01: Transaction Management
- Add new transactions with name, amount, category, type (INCOME/EXPENSE), and date
- View all transactions with filtering by date range, category, and type
- Edit any field of an existing transaction
- Delete a transaction with confirmation prompt
- Auto-categorize transactions based on configurable keyword rules stored in PostgreSQL

### FR-02: Budget Management
- Define a monthly budget per category with a monetary cap (`NUMERIC(12,2)`)
- Display current spending vs budget limit in real time
- Trigger visual alert when spending reaches 80 % of a budget limit
- Full CRUD on budget entries

### FR-03: Dashboard & Reports
- Display total income, total expenses, and net balance for the current month
- Pie chart of spending by category (JavaFX `PieChart`)
- Bar/line chart showing monthly spending trends
- Export financial reports to PDF (iText) or Excel (Apache POI)

### FR-04: Notes & Goals
- Create notes with title, content, date, and optional tags
- Define savings goals with target amount and deadline
- Calculate and display percentage completion of each goal
- In-app reminders for approaching goal deadlines

---

## ⚙️ Non-Functional Requirements

| ID | Category | Requirement |
|---|---|---|
| NFR-01 | **Performance** | Launch in under 4 s; GUI responses under 200 ms; HikariCP connection pooling |
| NFR-02 | **Reliability** | No data loss or corruption; atomic writes via PostgreSQL ACID transactions |
| NFR-03 | **Usability** | Core tasks completable within 5 minutes without documentation |
| NFR-04 | **Security** | Passwords hashed with BCrypt; TLS for remote PostgreSQL; no plaintext credentials |
| NFR-05 | **Maintainability** | JUnit 5 unit-test coverage (JaCoCo) > 80 %; Javadoc on all public methods |
| NFR-06 | **Portability** | Runs on Windows 10+, macOS 12+, Ubuntu 20.04+ with JDK 17 |
| NFR-07 | **Scalability** | Repository layer swappable with zero service-layer changes |
| NFR-08 | **Data Integrity** | Foreign key constraints enforced in PostgreSQL; cascading deletes configured |
| NFR-09 | **Build** | `mvn clean verify` builds cleanly on any JDK 17 environment |
| NFR-10 | **Localization** | User-facing strings externalised via `ResourceBundle` .properties |

---

## 🚀 Maven Build & Run

1. **Clone the repository:**

```bash
git clone https://github.com/anasemadanas/Expense_Track.git
cd Expense_Track/money-manager
```

2. **Start PostgreSQL (Docker one-liner):**

```bash
docker run -d --name mm-pg \
  -e POSTGRES_USER=moneymgr \
  -e POSTGRES_PASSWORD=moneymgr \
  -e POSTGRES_DB=money_manager \
  -p 5432:5432 postgres:16
```

3. **Build:**

```bash
mvn clean verify
```

4. **Run the application:**

```bash
# Via the JavaFX Maven plugin
mvn javafx:run

# Or the shaded fat JAR
java -jar target/money-manager-1.0.0-shaded.jar
```

### Prerequisites

- Java 17 LTS (Temurin recommended)
- Apache Maven 3.9+
- PostgreSQL 16 (local or Docker)

---

## 🧪 Testing

- **Unit tests** — JUnit 5 + Mockito on services with mocked repository interfaces
- **Integration tests** — Testcontainers boots a throwaway PostgreSQL container per run
- **Coverage gate** — JaCoCo enforces ≥ 80 % line coverage in `mvn verify`
- **Static analysis** — (optional) Checkstyle / SpotBugs via Maven plugins

```bash
mvn test            # unit + fast tests
mvn verify          # full verification incl. integration tests + coverage
```

---

## 🔮 Future Enhancements

| Enhancement | Details |
|---|---|
| **Android App** | Kotlin + Jetpack Compose sharing the service layer via a Java-only module |
| **Web App** | Spring Boot REST API + React frontend |
| **Cloud Sync** | Managed PostgreSQL on AWS RDS / Supabase / Neon |
| **Scheduled Reports** | Quartz Scheduler producing PDF/Excel on a cron schedule |
| **AI-based Insights** | TensorFlow Java / ONNX Runtime for transaction classification and anomaly detection |
| **Multi-User / Family Mode** | Role-based access (admin/viewer) secured via Spring Security |

---

## 🔒 Constraints & Assumptions

### Constraints
- v1.0 supports a single local user profile; multi-user cloud authentication deferred to v2.0
- GUI built with JavaFX 21 only — no web UI in v1.0
- Data stored in a PostgreSQL 16 instance (local or on-LAN); cloud backup optional
- A reachable PostgreSQL instance is required for core functionality
- Distributed as a fat JAR (maven-shade-plugin) plus optional native installers (jpackage)
- Minimum supported JDK: OpenJDK 17 LTS (verified against Temurin)

### Assumptions
- Users have basic familiarity with personal finance concepts
- Development uses Java 17+, Apache Maven 3.9+, PostgreSQL 16
- Monetary values stored as `NUMERIC(12,2)` → mapped to `java.math.BigDecimal` (no floating-point arithmetic)
- Dates stored as `DATE` / `TIMESTAMPTZ` → mapped to `java.time.LocalDate` / `java.time.OffsetDateTime`
- Flyway applies schema migrations on startup; rollback is a manual DBA procedure
- Host has ≥ 512 MB free RAM available for PostgreSQL

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Add tests covering your change
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

Please ensure your code follows SOLID principles, respects the 3-tier boundaries, and keeps `mvn verify` green.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](https://github.com/anasemadanas/Expense_Track/blob/main/LICENSE) file for details.

---
[↩️ Back to Table of Contents](#-Table-of-Contents)
---
<p align="center">
  <sub>Built with ❤️ using Java • Apache Maven • JavaFX • PostgreSQL • Designed with SOLID principles in mind</sub>
</p>
