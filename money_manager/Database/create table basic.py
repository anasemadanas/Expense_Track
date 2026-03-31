import sqlite3
conn = sqlite3.connect('Money_Manager_DB.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Budget (
    Budget_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Amount REAL NOT NULL,
    Spent REAL DEFAULT 0,
    Period TEXT,
    BudgetPerCategory TEXT
)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS Transactions (
    Transaction_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Amount REAL NOT NULL,
    Category TEXT,
    Date TEXT,
    Type TEXT,
    Note TEXT,
    Budget_ID INTEGER,
    FOREIGN KEY (Budget_ID) REFERENCES Budget(Budget_ID)
)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    User_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT NOT NULL UNIQUE,
    Password TEXT NOT NULL
)
''')

cursor.execute('''
INSERT OR IGNORE INTO Users (Username, Password) 
VALUES (?, ?)
''', ("admin", "1234"))

print("Database ready and admin user added.")

conn.commit()
conn.close()


    