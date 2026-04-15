PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    permissions INTEGER NOT NULL DEFAULT 0
);

INSERT OR IGNORE INTO users (username, password, permissions)
VALUES
('admin', '1234', -1),
('user', 'user', 1),
('zaid', 'zaid', 3),
('hamza', '9999', 4);

CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    month INTEGER NOT NULL CHECK(month BETWEEN 1 AND 12),
    year INTEGER NOT NULL CHECK(year >= 2020)

);

CREATE TABLE IF NOT EXISTS budgets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    month INTEGER NOT NULL CHECK(month BETWEEN 1 AND 12),
    year INTEGER NOT NULL CHECK(year >= 2020),
	total_amount REAL NOT NULL,
    UNIQUE(month, year)

);

CREATE TABLE IF NOT EXISTS goals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    target_amount REAL NOT NULL,
    saved_amount REAL DEFAULT 0.0
);

CREATE INDEX IF NOT EXISTS idx_transactions_month_year
ON transactions (month, year);

CREATE INDEX IF NOT EXISTS idx_budgets_month_year
ON budgets (month, year);