import hashlib
import hmac
import os
import sqlite3

from database.database import DatabaseConnection
from repository.IUserRepo import IUserRepo


class UserRepo(IUserRepo):
    def find_user(self, username: str, password: str):
        with DatabaseConnection() as db:
            result = db.execute("SELECT * FROM users WHERE username = ?", (username,), fetch="one")
            if not result or not _verify_password(password, result["password"]):
                return None

            if not result["password"].startswith("pbkdf2_sha256$"):
                db.execute(
                    "UPDATE users SET password = ? WHERE id = ?",
                    (_hash_password(password), result["id"]),
                )

        return {
            "id": result["id"],
            "username": result["username"],
            "permissions": result["permissions"],
            "has_recovery_key": bool(result["recovery_key"]),
        }

    def create_user(self, username: str, password: str, recovery_key: str, permissions: int = 7):
        try:
            with DatabaseConnection() as db:
                db.execute(
                    """
                    INSERT INTO users (username, password, recovery_key, permissions)
                    VALUES (?, ?, ?, ?)
                    """,
                    (username, _hash_password(password), _hash_password(recovery_key), permissions),
                )
        except sqlite3.IntegrityError as exc:
            raise ValueError("That username is already in use.") from exc

    def reset_password(self, username: str, recovery_key: str, password: str):
        with DatabaseConnection() as db:
            existing = db.execute(
                "SELECT id, recovery_key FROM users WHERE username = ?",
                (username,),
                fetch="one",
            )
            if (
                not existing
                or not existing["recovery_key"]
                or not _verify_password(recovery_key, existing["recovery_key"])
            ):
                return False
            db.execute(
                "UPDATE users SET password = ? WHERE id = ?",
                (_hash_password(password), existing["id"]),
            )
        return True

    def set_recovery_key(self, user_id: int, recovery_key: str):
        with DatabaseConnection() as db:
            db.execute(
                "UPDATE users SET recovery_key = ? WHERE id = ?",
                (_hash_password(recovery_key), user_id),
            )


def _hash_password(password: str) -> str:
    iterations = 260000
    salt = os.urandom(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)
    return f"pbkdf2_sha256${iterations}${salt.hex()}${digest.hex()}"


def _verify_password(password: str, stored_password: str) -> bool:
    if not stored_password.startswith("pbkdf2_sha256$"):
        return hmac.compare_digest(password, stored_password)

    try:
        _, iterations, salt, expected = stored_password.split("$", 3)
        digest = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            bytes.fromhex(salt),
            int(iterations),
        )
    except (TypeError, ValueError):
        return None
    return hmac.compare_digest(digest.hex(), expected)
