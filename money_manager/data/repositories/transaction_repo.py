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


    # ----------------------- get transactions ------------------------------------------- ----
    def get_transactions(self):
        query = "SELECT id, amount, category, month, year FROM transactions ORDER BY year, month"
        return self.db.execute(query, fetch="all")



    def delete_transaction(self, transaction_id: int):
        query = "DELETE FROM transactions WHERE id = ?"
        return self.db.execute(query, (transaction_id,), fetch=None)   
    
    
    def get_transactions_by_month(self, month, year):
        query = "SELECT * FROM transactions WHERE month=? AND year=? ORDER BY id"
        return self.db.execute(query, (month, year), fetch="all")


    def get_transactions_with_budget(self):
        query = "select * from transactions"
        return self.db.execute(query, fetch="all")


    def get_transactions_by_month_year(self, month, year):
        query = """
            SELECT amount, date, category 
            FROM transactions
            WHERE strftime('%m', date) = :m
            AND strftime('%Y', date) = :y
        """
        return self.db.execute(query, {"m": f"{month:02}", "y": str(year)}).fetchall()