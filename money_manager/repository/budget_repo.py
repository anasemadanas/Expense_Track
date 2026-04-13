from models.budget import Budget
from database.database import DatabaseConnection
from repository.IBudgetRepo import IBudgetRepo

class BudgetRepo(IBudgetRepo):
    def __init__(self):
        self.db = DatabaseConnection()

    # ----------------------- create or update budget -----------------------
    def create_budget(self, amount: float, month: int, year: int):

        existing = self.db.execute(
            "SELECT * FROM budgets WHERE month=? AND year=?",
            (month, year),
            fetch="one"
        )

        if existing:
            self.db.execute(
                "UPDATE budgets SET amount = amount + ?, total_amount = total_amount + ? WHERE month = ? AND year = ?",
                (amount, amount, month, year)
            )
        else:
            self.db.execute(
                "INSERT INTO budgets (amount, total_amount, month, year) VALUES (?, ?, ?, ?)",
                (amount, amount, month, year)
            )

        return self.get_budget(month, year)

    # ----------------------- check if budget exists -----------------------
    def check_budget(self, month, year):
        row = self.db.execute(
            "SELECT * FROM budgets WHERE month=? AND year=?",
            (month, year),
            fetch="one"
        )

        if row is None:
            return Budget(amount=0,totalamount=0, month=month, year=year,  id=None)

        return Budget(
            id=row[0],
            amount=row[1],
            month=row[2],
            year=row[3],
            totalamount=row[4]
        )

    # ----------------------- update budgets after spending -----------------------
    def deduct_from_budget(self, amount_spent: float, month: int, year: int):
        query = "UPDATE budgets SET amount = amount - ? WHERE month=? AND year=?"
        return self.db.execute(query, (amount_spent, month, year))

    def add_to_budget(self, amount, month, year):
        query = "UPDATE budgets SET amount = amount + ? WHERE month=? AND year=?"
        return self.db.execute(query, (amount, month, year))

    # ----------------------- return to transaction -----------------------
    def get_budget_balance(self, month, year):
        query = "SELECT amount FROM budgets WHERE month = ? AND year = ?"
        return self.db.execute(query, (month, year), fetch="one")

    # ----------------------- future -----------------------
    def get_budget(self, month: int, year: int):
        return self.db.execute(
            "SELECT * FROM budgets WHERE month=? AND year=?",
            (month, year),
            fetch="one"
        )  
    def update_budget(self, budget_id: int, amount: float):
        query = "UPDATE Budgets SET Amount = ? WHERE Budget_ID = ?"
        return self.db.execute(query, (amount, budget_id), fetch=None)

    def delete_budget(self, budget_id: int):
        query = "DELETE FROM Budgets WHERE Budget_ID = ?"
        return self.db.execute(query, (budget_id,), fetch=None)