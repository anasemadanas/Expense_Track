import os
import sqlite3


class DatabaseConnection:
    def __init__(self):
        self.db_dir = r"C:\Users\Public"
        os.makedirs(self.db_dir, exist_ok=True)

        self.db_path = os.path.join(self.db_dir, "Money_Manager_DB.db")

        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA foreign_keys = ON")

    def execute(self, query, params=None, fetch=None):
        params = params or ()

        cursor = self.conn.cursor()
        try:
            cursor.execute(query, params)

            if fetch == "one":
                result = cursor.fetchone()
                return result

            if fetch == "all":
                result = cursor.fetchall()
                return result

            self.conn.commit()
            return None

        finally:
            cursor.close()

    def executescript(self, script):
        try:
            self.conn.executescript(script)
            self.conn.commit()
        finally:
            pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.conn.rollback()
        self.conn.close()
