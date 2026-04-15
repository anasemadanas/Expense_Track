import os
import sys


def get_app_dir():
    if sys.platform == "win32":
        base = r"C:\Users\Public\MoneyManager"

    elif sys.platform == "darwin":
        base = "/Users/Shared/MoneyManager"

    else:
        base = os.path.expanduser("~/.local/share/MoneyManager")

    os.makedirs(base, exist_ok=True)
    return base


def get_db_path():
    return os.path.join(get_app_dir(), "Money_Manager_DB.db")