import sqlite3

from database.database_setup import initialize_database
from models.transaction import Transaction
from repository.budget_repo import BudgetRepo
from repository.goal_repo import GoalRepo
from repository.transaction_repo import TransactionRepo
from repository.user_repo import UserRepo


def use_temporary_database(monkeypatch, tmp_path):
    db_path = tmp_path / "money_manager.db"
    monkeypatch.setattr("database.database.get_db_path", lambda: str(db_path))
    monkeypatch.setattr("database.database_setup.get_db_path", lambda: str(db_path))
    return db_path


def test_users_have_separate_budgets_transactions_and_goals(monkeypatch, tmp_path):
    use_temporary_database(monkeypatch, tmp_path)
    initialize_database()

    users = UserRepo()
    users.create_user("alice", "secret1", "recover1")
    users.create_user("bob", "secret2", "recover2")
    alice = users.find_user("alice", "secret1")
    bob = users.find_user("bob", "secret2")

    assert alice is not None and bob is not None
    assert not users.reset_password("alice", "wrong-code", "changed1")
    assert users.reset_password("alice", "recover1", "changed1")
    assert users.find_user("alice", "changed1") is not None

    alice_budget = BudgetRepo(alice["id"])
    bob_budget = BudgetRepo(bob["id"])
    alice_budget.create_budget(100, 5, 2026)
    bob_budget.create_budget(250, 5, 2026)

    assert alice_budget.check_budget(5, 2026).totalamount == 100
    assert bob_budget.check_budget(5, 2026).totalamount == 250

    alice_transactions = TransactionRepo(alice["id"])
    bob_transactions = TransactionRepo(bob["id"])
    alice_transactions.add_transaction(Transaction(10, "Food", 5, 2026))
    bob_transactions.add_transaction(Transaction(20, "Travel", 5, 2026))

    assert [row["category"] for row in alice_transactions.get_transactions()] == ["Food"]
    assert [row["category"] for row in bob_transactions.get_transactions()] == ["Travel"]

    alice_goals = GoalRepo(alice["id"])
    bob_goals = GoalRepo(bob["id"])
    alice_goals.create_goal("Laptop", 500)
    bob_goals.create_goal("Holiday", 800)

    assert [goal.name for goal in alice_goals.get_all_goals()] == ["Laptop"]
    assert [goal.name for goal in bob_goals.get_all_goals()] == ["Holiday"]


def test_existing_global_rows_are_assigned_to_admin_during_migration(monkeypatch, tmp_path):
    db_path = use_temporary_database(monkeypatch, tmp_path)
    conn = sqlite3.connect(db_path)
    conn.executescript(
        """
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            permissions INTEGER NOT NULL DEFAULT 0
        );
        INSERT INTO users (username, password, permissions) VALUES ('admin', '1234', -1);
        CREATE TABLE budgets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            month INTEGER NOT NULL,
            year INTEGER NOT NULL,
            total_amount REAL NOT NULL,
            UNIQUE(month, year)
        );
        INSERT INTO budgets (amount, month, year, total_amount) VALUES (50, 5, 2026, 100);
        CREATE TABLE transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            month INTEGER NOT NULL,
            year INTEGER NOT NULL
        );
        INSERT INTO transactions (amount, category, month, year) VALUES (10, 'Food', 5, 2026);
        CREATE TABLE goals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            target_amount REAL NOT NULL,
            saved_amount REAL DEFAULT 0.0
        );
        INSERT INTO goals (name, target_amount, saved_amount) VALUES ('Car', 1000, 10);
        """
    )
    conn.close()

    initialize_database()

    admin_budget = BudgetRepo(1).check_budget(5, 2026)
    assert admin_budget.id is not None
    assert len(TransactionRepo(1).get_transactions()) == 1
    assert [goal.name for goal in GoalRepo(1).get_all_goals()] == ["Car"]
