# Money Manager

Money Manager is a PySide6 desktop expense-tracking application backed by SQLite. It keeps budgets, transactions, and savings goals separated by user and routes database access through repository and service layers.

This document focuses on the database and service design implemented in this project.

## Main Features

- User registration, login, password recovery, and permission-controlled actions.
- Monthly budget creation and budget balance tracking.
- Transaction creation, editing, deletion, and CSV export.
- Budget validation before a transaction is stored, including an 80% usage warning.
- Savings-goal storage and progress updates through `GoalService` and `GoalsDialog`.
- Dashboard summaries and chart data based on the signed transaction amounts.

## Technology

| Area | Implementation |
| --- | --- |
| Desktop UI | Python, PySide6 |
| Persistence | SQLite through `sqlite3` |
| Data access | Repository classes in `repository/` |
| Business logic | Service classes in `services/` |
| Schema setup and migration | `database/schema.sql`, `database/database_setup.py` |
| Tests | `pytest` |

## Project Structure

```text
money_manager/
|-- common/       # Shared session, theme, utility, and activity logging helpers
|-- database/     # SQLite connection, path selection, initialization, and schema
|-- docs/         # PlantUML design documentation
|-- models/       # Domain objects: Transaction, Budget, Goal, permissions
|-- repository/   # SQL persistence operations scoped to a user
|-- services/     # Validation and business workflows
|-- tests/        # Unit and database-isolation tests
|-- ui/           # PySide6 forms and generated UI classes
`-- main.py       # Application startup
```

## Running the Application

Create a virtual environment, install the dependency, and run the entry point:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

Run the test suite with:

```powershell
pip install -r requirements-dev.txt
pytest -q
```

At startup, `main.py` calls `initialize_database()` before opening the login form.

## Database

### Storage Location

The active SQLite database location is selected by `database/paths.py`:

| Platform | Database directory |
| --- | --- |
| Windows | `C:\Users\Public\MoneyManager` |
| macOS | `/Users/Shared/MoneyManager` |
| Linux | `~/.local/share/MoneyManager` |

The file name is `Money_Manager_DB.db`. The activity log is stored in the same application directory as `activity.log`.

### Tables

| Table | Purpose | User ownership |
| --- | --- | --- |
| `users` | Credentials, recovery key, and permission bit mask | Root account table |
| `budgets` | Monthly original and remaining budget balances | `user_id` foreign key |
| `transactions` | Categorized transaction amounts by month and year | `user_id` foreign key |
| `goals` | Savings targets and current saved amounts | `user_id` foreign key |

Each budget is unique per `(user_id, month, year)`. Transactions, budgets, and goals are deleted automatically when their owning user is deleted.

### Security and Migration Behavior

- Passwords and recovery codes written through `UserRepo` are stored as PBKDF2-SHA256 hashes with random salts.
- A legacy plain-text password is upgraded to a hash after a successful login.
- Existing databases without per-user data columns are migrated on initialization.
- During migration, legacy shared budget, transaction, and goal rows are assigned to the `admin` user, or the first available user if `admin` does not exist.
- `schema.sql` currently seeds demonstration accounts. These seed credentials should not be used for production data.

### Validation Note

The SQLite schema accepts transaction and budget years from `2020` onward, while the service validators accept years from `2000` to `2100`. Data dated before `2020` can pass service validation but be rejected by SQLite.

## Service Layer

All feature repositories that store user data receive `user_id`, so their SQL queries only read or update rows owned by the logged-in user.

| Service | Responsibilities | Repository interactions |
| --- | --- | --- |
| `UserService` | Login attempt tracking, account registration, reset validation, recovery setup | `UserRepo` |
| `BudgetService` | Validate dates and amounts, create or increase a monthly budget, update remaining balance | `BudgetRepo` |
| `TransactionService` | Validate available budget, warn at high usage, add/edit/delete transactions, reconcile budget balance | `TransactionRepo`, `BudgetService` |
| `GoalService` | Validate and manage savings goals and goal contributions | `GoalRepo` |
| `DashBoardService` | Read transactions and budgets for summaries, save/export data | `TransactionRepo`, `BudgetRepo` |

### Transaction and Budget Workflow

1. The user creates a monthly budget.
2. `BudgetService` validates the amount and date and persists a user-scoped `budgets` row.
3. When the user adds a transaction, `TransactionService` verifies that a budget exists and that sufficient balance remains.
4. If the transaction would use at least 80% of the total budget, the UI asks for confirmation.
5. After confirmation, the transaction is inserted and the available budget amount is reduced.
6. Editing or deleting a transaction adjusts the remaining budget by the changed or removed amount.

### Permissions

The dashboard checks permission bits before opening feature dialogs:

| Bit | Permission |
| --- | --- |
| `1` | Add transaction |
| `2` | Add budget |
| `4` | View and manage transaction list |
| `-1` | Full access |

## Design Diagrams

The PlantUML source files can be rendered with a local PlantUML installation:

```powershell
plantuml docs\*.puml
```

| Diagram | File |
| --- | --- |
| Project system design | `docs/system_design.puml` |
| Project class diagram | `docs/class_diagram.puml` |
| Main activity diagrams | `docs/activity_diagrams.puml` |
| Database/service architecture | `docs/database_service_architecture.puml` |
| Add-transaction service sequence | `docs/database_service_sequence.puml` |
| Application use cases | `docs/database_service_use_case.puml` |
| SQLite entity relationship schema | `docs/database_schema.puml` |

## Implementation Entry Points

| Concern | Source |
| --- | --- |
| Startup and schema initialization | `main.py`, `database/database_setup.py` |
| SQL schema | `database/schema.sql` |
| Connection wrapper | `database/database.py` |
| User authentication persistence | `repository/user_repo.py`, `services/user_service.py` |
| Budget/transaction coordination | `services/budget_service.py`, `services/transaction_service.py` |
| User data isolation coverage | `tests/test_multi_user_database.py` |
