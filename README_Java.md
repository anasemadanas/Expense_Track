# 💰 Money Manager App — Java Edition
> Organize your finances. Track your money. Plan smarter.

A modern, scalable personal-finance desktop tool built in **Java 17** with **Apache Maven**, **JavaFX**, and **PostgreSQL**, following a clean **3-Tier Architecture** and **SOLID principles**.

---

## 📑 Table of Contents

- [🧾 Introduction](#-introduction)
- [✨ Features](#-features)
- [🖼️ Screenshots](#️-screenshots)
- [🧱 Architecture](#-architecture)
- [📂 Project Structure](#-project-structure)
- [📦 Requirements](#-requirements)
- [⚙️ Installation](#️-installation)
- [▶️ Run the App](#️-run-the-app)
- [🧪 Testing](#-testing)
- [🙌 How to Contribute](#-how-to-contribute)
- [🔮 Future Enhancements](#-future-enhancements)
- [📝 License](#-license)
- [🔗 Contact](#-contact)

---

## 🧾 Introduction

**Money Manager (Java Edition)** is a clean financial management application designed to help you:

- Track expenses and income
- Organize transactions into categories
- Plan monthly budgets
- View financial analytics through charts
- Take notes and set savings goals

Built using:

| Technology | Purpose |
|---|---|
| Java 17 LTS | Core language |
| Apache Maven 3.9+ | Build & dependency management |
| JavaFX 21 | Desktop GUI framework (FXML + CSS) |
| PostgreSQL 16 | Relational database |
| Spring Data JPA + Hibernate | Data-access layer |
| Flyway | Database schema migrations |
| HikariCP | JDBC connection pooling |
| Spring Security Crypto (BCrypt) | Password hashing |
| JUnit 5 + Mockito + Testcontainers | Automated testing |
| 3-Tier Architecture | Clean separation of concerns |
| Repository Pattern | Data-access abstraction |
| SOLID Principles | Scalable & maintainable code |

---

## ✨ Features

- 📘 Track expenses & income
- 🏷️ Categorize transactions
- 📆 Monthly budget planning with over-limit alerts
- 📊 Dashboard with pie and line/bar charts (JavaFX Charts)
- 🗒️ Notes & financial goals with deadline reminders
- 📤 Export reports to **PDF (iText)** and **Excel (Apache POI)**
- 🏛️ Clean, testable, 3-tier architecture
- 🗄️ PostgreSQL with JPA/Hibernate and the Repository Pattern
- 🔌 Easy to extend or migrate (Spring Boot REST / Android / Web)

---

## 🖼️ Screenshots

| Login | Dashboard | Transaction | Budget |
|-------|-----------|-------------|--------|
| ![Login](screenshots/Login.png) | ![Dashboard](screenshots/Dashboard.png) | ![Transaction](screenshots/transaction.png) | ![Budget](screenshots/budget.png) |

> Screenshots above are from the original Python/PySide6 prototype; the Java port replicates the same flows using JavaFX views (`fxml/` + `css/`).

---

## 🧱 Architecture

```
┌─────────────────────────────┐
│      Presentation Layer     │  ← JavaFX (FXML + CSS) + Controllers
├─────────────────────────────┤
│    Business Logic Layer     │  ← Services, Validation, Calculations
├─────────────────────────────┤
│        Data Layer           │  ← JPA / Hibernate + Repository Pattern
└──────────────┬──────────────┘
               │
         [ PostgreSQL 16 ]  (JDBC, HikariCP, Flyway)
```

---

## 📂 Project Structure

```bash
money-manager/
├── pom.xml
├── src/main/java/com/teamstudent/moneymanager/
│   ├── MoneyManagerApp.java        # JavaFX entry-point (Application)
│   ├── config/                     # AppConfig, DataSourceConfig
│   ├── ui/                         # Controllers + FXML loaders
│   ├── service/                    # TransactionService, BudgetService, GoalService
│   ├── repository/                 # IUserRepo, ITransactionRepo, IBudgetRepo + JPA impls
│   ├── model/                      # JPA entities (User, Transaction, Budget, Goal)
│   └── util/                       # Validators, formatters
├── src/main/resources/
│   ├── fxml/                       # *.fxml view files
│   ├── css/                        # application.css
│   ├── i18n/                       # messages_*.properties
│   ├── db/migration/               # V1__init.sql, V2__indexes.sql (Flyway)
│   └── application.yml
└── src/test/java/com/teamstudent/moneymanager/
    └── <mirroring test packages using JUnit 5 + Testcontainers>
```

---

## 📦 Requirements

```
Java 17 LTS (Temurin recommended)
Apache Maven 3.9+
PostgreSQL 16 (local instance or Docker)
```

Spin up a local PostgreSQL instance quickly with Docker:

```bash
docker run -d --name mm-pg \
  -e POSTGRES_USER=moneymgr \
  -e POSTGRES_PASSWORD=moneymgr \
  -e POSTGRES_DB=money_manager \
  -p 5432:5432 \
  postgres:16
```

---

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/anasemadanas/Expense_Track.git

# 2. Navigate to the Java project folder
cd Expense_Track/money-manager

# 3. Build and run all tests
mvn clean verify
```

Configure your database connection in `src/main/resources/application.yml`:

```yaml
spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/money_manager
    username: moneymgr
    password: moneymgr
  jpa:
    hibernate:
      ddl-auto: validate
  flyway:
    enabled: true
    locations: classpath:db/migration
```

---

## ▶️ Run the App

```bash
# Using the JavaFX Maven plugin
mvn javafx:run

# Or run the packaged fat JAR produced by maven-shade-plugin
java -jar target/money-manager-1.0.0-shaded.jar
```

> Flyway migrates the PostgreSQL schema automatically on startup — no manual SQL required.

---

## 🧪 Testing

```bash
# Run unit + integration tests
mvn test

# Full verification (unit tests, integration tests, coverage gate)
mvn clean verify
```

- **JUnit 5** for unit and integration tests
- **Mockito** for mocking repository interfaces
- **Testcontainers** spins up a disposable PostgreSQL instance for integration tests
- **JaCoCo** enforces ≥ 80 % line coverage

---

## 🙌 How to Contribute

Pull Requests are welcome! Follow these steps:

1. **Fork** the repository
2. **Create** a feature branch → `git checkout -b feature/your-feature`
3. **Commit** your changes → `git commit -m "Add: your feature"`
4. **Push** to your branch → `git push origin feature/your-feature`
5. **Submit** a Pull Request

Please keep commits focused, respect the 3-tier boundaries, and add tests for new behaviour.

---

## 🔮 Future Enhancements

- 📱 Android version (Kotlin / Jetpack Compose sharing the service layer)
- 🌐 Web version (Spring Boot REST + React)
- ☁️ Cloud sync (managed PostgreSQL on RDS / Supabase / Neon)
- 🧾 Scheduled PDF & Excel reports (Quartz Scheduler)
- 🤖 AI-powered spending predictions (TensorFlow Java / ONNX Runtime)
- 🎨 Modern UI redesign (JavaFX + CSS themes, light / dark mode)

---

## 📝 License

MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🔗 Contact

| Platform | Link |
|---|---|
| 🐙 GitHub | [GitHub](https://github.com/anasemadanas/) |
| 💼 LinkedIn | [LinkedIn](https://www.linkedin.com/in/eng-anasemad/) |
| 📧 Email | [Email](mailto:anaspython3@gmail.com) |

[↩️ Back to Table of Contents](#-table-of-contents)
