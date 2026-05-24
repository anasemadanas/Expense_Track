import os
from database.database import DatabaseConnection
from database.paths import get_db_path


def initialize_database():
    schema_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "schema.sql"
    )

    with open(schema_path, "r", encoding="utf-8") as f:
        schema_sql = f.read()

    database_exists = os.path.exists(get_db_path())
    with DatabaseConnection() as db:
        if database_exists:
            _migrate_existing_database(db)
        db.executescript(schema_sql)


def _migrate_existing_database(db):
    default_user_id = _get_default_user_id(db)
    if default_user_id is None:
        return

    if not _has_column(db, "users", "recovery_key"):
        db.execute("ALTER TABLE users ADD COLUMN recovery_key TEXT")

    if not _has_column(db, "transactions", "user_id"):
        db.execute("ALTER TABLE transactions ADD COLUMN user_id INTEGER REFERENCES users(id)")
        db.execute("UPDATE transactions SET user_id = ? WHERE user_id IS NULL", (default_user_id,))

    if not _has_column(db, "goals", "user_id"):
        db.execute("ALTER TABLE goals ADD COLUMN user_id INTEGER REFERENCES users(id)")
        db.execute("UPDATE goals SET user_id = ? WHERE user_id IS NULL", (default_user_id,))

    if not _has_column(db, "budgets", "user_id"):
        _rebuild_budgets_for_users(db, default_user_id)


def _get_default_user_id(db):
    row = db.execute("SELECT id FROM users WHERE username = 'admin'", fetch="one")
    if row:
        return row["id"]
    row = db.execute("SELECT id FROM users ORDER BY id LIMIT 1", fetch="one")
    return row["id"] if row else None


def _has_column(db, table_name, column_name):
    columns = db.execute(f"PRAGMA table_info({table_name})", fetch="all")
    return any(column["name"] == column_name for column in columns)


def _rebuild_budgets_for_users(db, default_user_id):
    db.execute(
        """
        CREATE TABLE budgets_new (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            amount REAL NOT NULL,
            month INTEGER NOT NULL CHECK(month BETWEEN 1 AND 12),
            year INTEGER NOT NULL CHECK(year >= 2020),
            total_amount REAL NOT NULL,
            UNIQUE(user_id, month, year)
        )
        """
    )
    db.execute(
        """
        INSERT INTO budgets_new (id, user_id, amount, month, year, total_amount)
        SELECT id, ?, amount, month, year, total_amount FROM budgets
        """,
        (default_user_id,),
    )
    db.execute("DROP TABLE budgets")
    db.execute("ALTER TABLE budgets_new RENAME TO budgets")
