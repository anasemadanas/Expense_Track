import sqlite3
import os

class DatabaseConnection:
    def __init__(self):
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        db_path = os.path.join(project_root, "Database", "Money_Manager_DB.db")

        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def execute(self, query, params=(), fetch="all"):
        self.cursor.execute(query, params)

        if fetch == "one":
            return self.cursor.fetchone()
        elif fetch == "all":
            return self.cursor.fetchall()
        else:
            self.conn.commit()
            return None