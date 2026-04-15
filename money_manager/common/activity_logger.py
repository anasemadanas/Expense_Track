from datetime import datetime
from pathlib import Path
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


class ActivityLogger:

    _log_file = Path(get_app_dir()) / "activity.log"

    @classmethod
    def _write(cls, username: str, action: str, details: str = ""):
        cls._log_file.parent.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        clean_username = username or "unknown"

        line = f"[{timestamp}] user={clean_username} action={action}"

        if details:
            line += f" details={details}"

        with cls._log_file.open("a", encoding="utf-8") as log_file:
            log_file.write(line + "\n")

    @staticmethod
    def current_username():
        try:
            import common.global_user as global_user

            user = getattr(global_user, "current_user", None)

            if isinstance(user, dict):
                return user.get("username", "unknown")

        except Exception:
            pass

        return "unknown"

    @classmethod
    def log_login(cls, username: str):
        cls._write(username, "login")

    @classmethod
    def log_budget(cls, amount: float, month: int, year: int, action: str = "budget_created"):
        cls._write(
            cls.current_username(),
            action,
            f"amount={amount:.2f}, month={month}, year={year}",
        )

    @classmethod
    def log_transaction(cls, amount: float, category: str, month: int, year: int):
        cls._write(
            cls.current_username(),
            "transaction_added",
            f"amount={amount:.2f}, category={category}, month={month}, year={year}",
        )

    @classmethod
    def log_exit(cls, username: str | None = None):
        cls._write(username or cls.current_username(), "exit")