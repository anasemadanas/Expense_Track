import os
from database.database import DatabaseConnection
from database.paths import get_db_path


def initialize_database():
    db_path = get_db_path()

    if os.path.exists(db_path):
        return

    db = DatabaseConnection()

    schema_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "schema.sql"
    )

    with open(schema_path, "r", encoding="utf-8") as f:
        schema_sql = f.read()

    with db:
        db.executescript(schema_sql)