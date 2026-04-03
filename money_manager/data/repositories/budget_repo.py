from Services.models.budget import Budget
from data.database import DatabaseConnection
from data.interfaces.IBudgetRepo import IBudgetRepo

class BudgetRepo(IBudgetRepo):

    def __init__(self):
        self.db = DatabaseConnection()
        
    def get_budget(self, month, year):
        
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT * FROM budgets WHERE month=? AND year=?", (month, year))
        row = cursor.fetchone()  
        
        if row is None:
            return None

        return Budget(
            amount=row["amount"],
            totalamount=row["total_amount"],
            month=row["month"],
            year=row["year"],
            id=row["id"]
        )
        
    def create_budget(self, amount: float, month: int, year: int):
        existing_budget = self.get_budget(month, year)
        if existing_budget:
            query = "UPDATE budgets SET amount = ? WHERE month = ? AND year = ?"
            self.db.execute(query, (amount, month, year))
            return existing_budget
        else:
            query = """
            INSERT INTO budgets (amount, total_amount, month, year)
            VALUES (?, ?, ?, ?)
            """
            self.db.execute(query, (amount, amount, month, year))
            return self.get_budget(month, year)


    def update_budget_amount(self, amount_spent: float, month: int, year: int):
        budget = self.get_budget(month, year)
        if not budget:
            return None  
        new_amount = budget.amount - amount_spent
        if new_amount < 0:
            new_amount = 0  
        query = "UPDATE budgets SET amount = ? WHERE month = ? AND year = ?"
        self.db.execute(query, (new_amount,new_amount, month, year), fetch=None)
        return new_amount





    def get_budget_by_date(self, month: int, year: int):
        query = "SELECT * FROM Budget WHERE Month = ? AND Year = ?"
        return self.db.execute(query, (month, year), fetch="one")

    def get_budget_by_id(self, budget_id: int):
        query = "SELECT * FROM Budget WHERE Budget_ID = ?"
        return self.db.execute(query, (budget_id,), fetch="one")

    def update_budget(self, budget_id: int, amount: float):
        query = "UPDATE Budget SET Amount = ? WHERE Budget_ID = ?"
        return self.db.execute(query, (amount, budget_id), fetch=None)

    def delete_budget(self, budget_id: int):
        query = "DELETE FROM Budgets WHERE Budget_ID = ?"
        return self.db.execute(query, (budget_id,), fetch=None)