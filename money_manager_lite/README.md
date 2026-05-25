# Money Manager Lite

Money Manager Lite is a desktop personal-finance application built with Python, PySide6, and SQLite. It provides a lightweight graphical interface for managing budgets, transactions, savings goals, and dashboard summaries locally.

## Features

- Login-based desktop interface
- Monthly budget management
- Income and expense transaction tracking
- Savings goal tracking
- Dashboard summaries and charts
- Configurable application theme
- Local SQLite data storage

## Technology

| Component | Technology |
|---|---|
| User interface | PySide6 |
| Data storage | SQLite |
| Tests | pytest |
| Desktop packaging | PyInstaller |

## Project Structure

```text
money_manager_lite/
|-- common/       Shared helpers, theme management, and activity logging
|-- database/     SQLite setup, schema, and database path handling
|-- models/       Budget, goal, transaction, and user models
|-- repository/   Data access implementations and interfaces
|-- resources/    Application icons
|-- services/     Business logic implementations and interfaces
|-- tests/        Unit tests
|-- ui/           PySide6 screens and generated UI modules
|-- main.py       Application entry point
|-- requirements.txt
`-- requirements-dev.txt
```

## Requirements

- Python 3.10 or newer
- `pip`

## Setup

From the repository root:

```bash
cd money_manager_lite
python -m venv .venv
```

Activate the virtual environment:

```bash
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Linux or macOS
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## Run

From `money_manager_lite/`:

```bash
python main.py
```

On first launch, the application initializes its SQLite database and creates the required tables.

## Tests

```bash
pytest
```

## Build A Desktop Package

PyInstaller configuration is included in `MoneyManager.spec`. From `money_manager_lite/`, run:

```bash
pyinstaller MoneyManager.spec
```

The packaged application is written to the `dist/` directory.

## Data Storage

The application stores its runtime database in a platform-specific application data location:

| Platform | Location |
|---|---|
| Windows | `C:\Users\Public\MoneyManager` |
| macOS | `/Users/Shared/MoneyManager` |
| Linux | `~/.local/share/MoneyManager` |

The schema includes users, transactions, budgets, and goals. The seed data in `database/schema.sql` is intended for local demonstration and development.

## Screenshots

| Login | Dashboard | Transaction |
|---|---|---|
| ![Login](../screenshots/Login.png) | ![Dashboard](../screenshots/Dashboard.png) | ![Transaction](../screenshots/transaction.png) |

| Budget | Goal | Transaction List |
|---|---|---|
| ![Budget](../screenshots/budget.png) | ![Goal](../screenshots/goal.png) | ![Transaction List](../screenshots/listTransaction.png) |

## License

This project is distributed under the license in the repository root [LICENSE](../LICENSE).
