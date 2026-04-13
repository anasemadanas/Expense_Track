import os
import sqlite3

class DatabaseConnection:
    def __init__(self):
        db_dir = r"C:\Users\Public"
        db_path = os.path.join(db_dir, "Money_Manager_DB.db")

        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row

        self.conn.execute("PRAGMA foreign_keys = ON")

        self.initialize_database()

    def initialize_database(self):
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        schema_path = os.path.join(project_root, "Database", "schema.sql")

        if not os.path.exists(schema_path):
            raise FileNotFoundError(f"Schema not found: {schema_path}")

        with open(schema_path, "r", encoding="utf-8") as f:
            self.conn.executescript(f.read())

        self.conn.commit()

    def execute(self, query, params=None, fetch=None):
        params = params or ()

        cursor = self.conn.cursor()
        cursor.execute(query, params)

        if fetch == "one":
            return cursor.fetchone()

        if fetch == "all":
            return cursor.fetchall()

        self.conn.commit()
        return None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()