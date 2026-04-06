from Services.models.transaction import Transaction
from data.database import DatabaseConnection
from data.interfaces.ITransactionRepo import ITransactionRepo

class TransactionRepo(ITransactionRepo):
    def __init__(self):
        self.db = DatabaseConnection()

    # ----------------------- add transaction ------------------------------------------- ----
    def add_transaction(self, transaction: Transaction):
        query = "INSERT INTO transactions (amount, category, month, year) VALUES (?, ?, ?, ?)"
        params = (transaction.amount, transaction.category, transaction.month, transaction.year)
        return self.db.execute(query, params)

    # ----------------------- get transactions from list ------------------------------------------- ----
    def get_transactions(self):
        query = "SELECT id, amount, category, month, year FROM transactions ORDER BY year, month"
        return self.db.execute(query, fetch="all")
    
    def get_transaction_by_id(self, transaction_id: int):
        query = "SELECT * FROM transactions WHERE id = ?"
        row = self.db.execute(query, (transaction_id), fetch="one") 
        
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
        query = "UPDATE transactions SET amount = ?, month = ?, year = ? WHERE id = ?"
        params = (new_amount, new_month, new_year, transaction_id)
        self.db.execute(query, params)
        
    def delete_transaction(self, transaction_id: int):
        query = "DELETE FROM transactions WHERE id = ?"
        return self.db.execute(query, (transaction_id,), fetch=None)   
    
    def get_transactions_by_month (self, month, year):
        query = "select * from  transactions where month = ?, year = ?"
        params = (month, year)
        self.db.execute(query, params)
