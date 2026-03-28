from src.data.database import DatabaseConnection
from src.data.interfaces.ITransactionRepo import ITransactionRepo


class TransactionRepo(ITransactionRepo):

    def __init__(self):
        self.db = DatabaseConnection()

    def add_transaction(self, transaction):
        query = """
            INSERT INTO Transaction
            (Name, Amount, Category, Date, Type, Budget_ID, User_ID, Family_ID, Currency_ID)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        params = (
            transaction.name,
            transaction.amount,
            transaction.category,
            transaction.date,
            transaction.type,
            transaction.budget_id,
            transaction.user_id,
            transaction.family_id,
            transaction.currency_id
        )
        return self.db.execute(query, params)

    def get_transaction_by_id(self, transaction_id: int):
        query = "SELECT * FROM Transaction WHERE Transaction_ID = ?"
        return self.db.fetch_one(query, (transaction_id,))

    def get_transactions_by_user(self, user_id: int):
        query = """
            SELECT * FROM Transaction 
            WHERE User_ID = ?
            ORDER BY Date DESC
        """
        return self.db.fetch_all(query, (user_id,))

    def get_transactions_by_family(self, family_id: int):
        query = "SELECT * FROM Transaction WHERE Family_ID = ? ORDER BY Date DESC"
        return self.db.fetch_all(query, (family_id,))

    def update_transaction(self, transaction):
        query = """
            UPDATE Transaction
            SET Name = ?, Amount = ?, Category = ?, Date = ?, Type = ?, 
                Budget_ID = ?, Family_ID = ?, Currency_ID = ?
            WHERE Transaction_ID = ?
        """
        params = (
            transaction.name,
            transaction.amount,
            transaction.category,
            transaction.date,
            transaction.type,
            transaction.budget_id,
            transaction.family_id,
            transaction.currency_id,
            transaction.id
        )
        return self.db.execute(query, params)

    def delete_transaction(self, transaction_id: int):
        query = "DELETE FROM Transaction WHERE Transaction_ID = ?"
        return self.db.execute(query, (transaction_id,))

    def filter_transactions(self, user_id: int, category=None, ttype=None, start=None, end=None):
        """فلترة متقدمة"""
        query = "SELECT * FROM Transaction WHERE User_ID = ?"
        params = [user_id]

        if category:
            query += " AND Category = ?"
            params.append(category)

        if ttype:
            query += " AND Type = ?"
            params.append(ttype)

        if start:
            query += " AND Date >= ?"
            params.append(start)

        if end:
            query += " AND Date <= ?"
            params.append(end)

        query += " ORDER BY Date DESC"
        return self.db.fetch_all(query, tuple(params))