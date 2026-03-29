import sqlite3
import os

CURRENT = os.path.abspath(__file__)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(CURRENT)))
DB_PATH = os.path.join(PROJECT_ROOT, "Database", "money_manager_DB.db")
DB_PATH = os.path.normpath(DB_PATH)


class DatabaseConnection:
    def __init__(self):
        self.db_name = DB_NAME

    def connect(self):
        """Create DB connection with proper settings."""
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn

    def execute(self, query: str, params: tuple = ()):
        """INSERT, UPDATE, DELETE"""
        conn = self.connect()
        cursor = conn.cursor()

        try:
            cursor.execute(query, params)
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            print("DB ERROR:", e)
            return None
        finally:
            conn.close()

    def fetch_one(self, query: str, params: tuple = ()):
        conn = self.connect()
        cursor = conn.cursor()

        try:
            cursor.execute(query, params)
            row = cursor.fetchone()
            return dict(row) if row else None
        except sqlite3.Error as e:
            print("DB ERROR:", e)
            return None
        finally:
            conn.close()

    def fetch_all(self, query: str, params: tuple = ()):
        conn = self.connect()
        cursor = conn.cursor()

        try:
            cursor.execute(query, params)
            rows = cursor.fetchall()
            return [dict(r) for r in rows]
        except sqlite3.Error as e:
            print("DB ERROR:", e)
            return []
        finally:
            conn.close()
