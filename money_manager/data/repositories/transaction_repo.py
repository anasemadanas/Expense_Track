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
    
    
    
    
    def get_transactions(self):
        query = "SELECT * FROM transactions"
        rows = self.db.execute(query, fetch="all")
        transactions = []
        for row in rows:
            transactions.append(Transaction(
                amount=row["amount"],
                category=row["category"],
                month=row["month"],
                year=row["year"],
                id=row["id"]
            ))
        return transactions
    
    def delete_transaction(self, transaction_id: int):
        query = "DELETE FROM transactions WHERE transaction_ID = ?"
        return self.db.execute(query, (transaction_id,), fetch=None)