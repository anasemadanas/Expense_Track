import os
from database.database import DatabaseConnection


def initialize_database():
    db_path = r"C:\Users\Public\Money_Manager_DB.db"

    if os.path.exists(db_path):
        return

    db = DatabaseConnection()

    database_dir = os.path.dirname(os.path.abspath(__file__))
    schema_path = os.path.join(database_dir, "schema.sql")

    with open(schema_path, "r", encoding="utf-8") as f:
        schema_sql = f.read()

    with db:
        db.executescript(schema_sql)