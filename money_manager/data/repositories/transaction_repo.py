from Services.models.transaction import Transaction
from data.database import DatabaseConnection

class TransactionRepo:
    def __init__(self):
        self.db = DatabaseConnection()

    def add_transaction(self, transaction: Transaction):
        query = """
        INSERT INTO transactions (amount, category, month, year)
        VALUES (?, ?, ?, ?)
        """

        params = (
            transaction.amount,
            transaction.category,
            transaction.month,
            transaction.year
        )

        return self.db.execute(query, params)
    
    
    

    
    def delete_transaction(self, transaction_id: int):
        query = "DELETE FROM transactions WHERE transaction_ID = ?"
        return self.db.execute(query, (transaction_id,), fetch=None)