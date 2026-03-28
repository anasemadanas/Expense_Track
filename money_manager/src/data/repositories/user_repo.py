from src.data.database import DatabaseConnection
from src.data.interfaces.IUserRepo import IUserRepo


class UserRepo(IUserRepo):
    def __init__(self):
        self.db = DatabaseConnection()

    def create_user(self, username, password_hash, email=None, phone=None, currency_id=None):
        query = """
            INSERT INTO UserAccount (UserName, Password, Email, Phone, Currency_ID)
            VALUES (?, ?, ?, ?, ?)
        """
        params = (username, password_hash, email, phone, currency_id)
        return self.db.execute(query, params)

    def get_user_by_username(self, username: str):
        query = "SELECT * FROM UserAccount WHERE UserName = ?"
        return self.db.fetch_one(query, (username,))

    def get_user_by_id(self, user_id: int):
        query = "SELECT * FROM UserAccount WHERE User_ID = ?"
        return self.db.fetch_one(query, (user_id,))

    def update_user_currency(self, user_id: int, currency_id: int):
        query = "UPDATE UserAccount SET Currency_ID = ? WHERE User_ID = ?"
        return self.db.execute(query, (currency_id, user_id))

    def delete_user(self, user_id: int):
        query = "DELETE FROM UserAccount WHERE User_ID = ?"
        return self.db.execute(query, (user_id,))