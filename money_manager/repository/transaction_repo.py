from models.transaction import Transaction
from database.database import DatabaseConnection
from repository.ITransactionRepo import ITransactionRepo

class TransactionRepo(ITransactionRepo):
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.db = DatabaseConnection()

    # ----------------------- add transaction ------------------------------------------- ----
    def add_transaction(self, transaction: Transaction):
        query = "INSERT INTO transactions (user_id, amount, category, month, year) VALUES (?, ?, ?, ?, ?)"
        params = (self.user_id, transaction.amount, transaction.category, transaction.month, transaction.year)
        return self.db.execute(query, params)

    # ----------------------- get transactions from list -------------------------------------------
    def get_transactions(self):
        query = """
        SELECT id, amount, category, month, year FROM transactions
        WHERE user_id = ? ORDER BY year, month
        """
        return self.db.execute(query, (self.user_id,), fetch="all")
    
    # ---------------------- List transaction to edit -----------------------------------------------------
    def get_transaction_by_id(self, transaction_id: int):
        query = "SELECT id, amount, category, month, year FROM transactions WHERE id = ? AND user_id = ?"
        row = self.db.execute(query, (transaction_id, self.user_id), fetch="one")

        
        if row is None:
            return Transaction(id=None, amount=0, category="", month=0, year=0)
                
        return Transaction(
            id=row[0],
            amount=row[1],
            category=row[2],
            month=row[3],
            year=row[4]
        )


    def update_transaction(self, transaction_id, new_amount, new_month, new_year):
        query = """ UPDATE transactions
                    SET amount = ?, month = ?, year = ?
                    WHERE id = ? AND user_id = ?"""
        params = (new_amount, new_month, new_year, transaction_id, self.user_id)
        self.db.execute(query, params)
        
    def delete_transaction(self, transaction_id: int):
        query = "DELETE FROM transactions WHERE id = ? AND user_id = ?"
        return self.db.execute(query, (transaction_id, self.user_id), fetch=None)
    # ---------------------- -------------------------------------------------------------------
    

    def get_transactions_by_month(self, month, year):
        query = """
        SELECT id, amount, category, month, year 
        FROM transactions 
        WHERE user_id = ? AND month = ? AND year = ?
        """

        params = (self.user_id, month, year)

        results = self.db.execute(query, params, fetch="all")

        if not results:
            return []

        transactions = []
        for row in results:
            transactions.append({
                "id": row[0],
                "amount": row[1],
                "category": row[2],
                "month": row[3],
                "year": row[4]
            })

        return transactions
