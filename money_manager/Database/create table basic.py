import sqlite3

conn = sqlite3.connect('Money_Manager_DB.db')
cursor = conn.cursor()

cursor.executescript("""
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
        UNIQUE(month, year)              
    );
""")

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    User_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT NOT NULL UNIQUE,
    Password TEXT NOT NULL
);
''')

cursor.execute('''
INSERT OR IGNORE INTO Users (Username, Password) 
VALUES (?, ?)
''', ("admin", "1234"))

print("Database ready and admin user added.")

conn.commit()
conn.close()