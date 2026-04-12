import os
import sqlite3



class DatabaseConnection:
    def __init__(self):
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        db_path = os.path.join(project_root, "Database", "Money_Manager_DB.db")

        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()
        
    def execute(self, query, params=(), fetch=None):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)

            if fetch == "one":
                return cursor.fetchone()

            if fetch == "all":
                return cursor.fetchall()

            self.conn.commit()
            return None
        
        except sqlite3.Error as e:
            print("Database error:", e)
            return None
