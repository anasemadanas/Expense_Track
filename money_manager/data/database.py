import sqlite3
import os

class DatabaseConnection:
    def __init__(self):
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        db_path = os.path.join(project_root, "Database", "Money_Manager_DB.db")

        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()


        
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close() 
        
    def execute(self, query, params=(), fetch=None):
        self.cursor.execute(query, params)

        if fetch == "one":
            return self.cursor.fetchone()
        elif fetch == "all":
            return self.cursor.fetchall()
        else:
            self.conn.commit()
            return self.cursor.lastrowid 
        

        
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
