import os
import sqlite3
import shutil

class DatabaseConnection:
    def __init__(self):
        # Use C:\Users\Public for database storage
        db_dir = r"C:\Users\Public"
        db_path = os.path.join(db_dir, "Money_Manager_DB.db")

        # If db doesn't exist in public dir, copy from project dir
        if not os.path.exists(db_path):
            project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            source_db = os.path.join(project_root, "Database", "Money_Manager_DB.db")
            if os.path.exists(source_db):
                shutil.copy2(source_db, db_path)

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
