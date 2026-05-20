import os
import sqlite3
from database.paths import get_db_path


class DatabaseConnection:

    def __init__(self):
        self.db_path = get_db_path()

        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA foreign_keys = ON")

    def execute(self, query, params=None, fetch=None):
        params = params or ()

        cursor = self.conn.cursor()     #Commands
        try:
            cursor.execute(query, params)

            if fetch == "one":
                return cursor.fetchone()

            if fetch == "all":
                return cursor.fetchall()

            self.conn.commit()   #Save

        finally:
            cursor.close()

    def executescript(self, script):
        self.conn.executescript(script)
        self.conn.commit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.conn.rollback()
        self.conn.close()