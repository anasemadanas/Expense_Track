from models.budget import Budget
from database.database import DatabaseConnection
from repository.IBudgetRepo import IBudgetRepo

class BudgetRepo(IBudgetRepo):
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.db = DatabaseConnection()

    # ----------------------- create or update budget -----------------------
    def create_budget(self, amount: float, month: int, year: int):

        existing = self.db.execute(
            "SELECT * FROM budgets WHERE user_id=? AND month=? AND year=?",
            (self.user_id, month, year),
            fetch="one"
        )

        if existing:
            self.db.execute(
                """
                UPDATE budgets SET amount = amount + ?, total_amount = total_amount + ?
                WHERE user_id = ? AND month = ? AND year = ?
                """,
                (amount, amount, self.user_id, month, year)
            )
        else:
            self.db.execute(
                "INSERT INTO budgets (user_id, amount, total_amount, month, year) VALUES (?, ?, ?, ?, ?)",
                (self.user_id, amount, amount, month, year)
            )

        return self.get_budget(month, year)

    # ----------------------- check if budget exists -----------------------
    def check_budget(self, month, year):
        row = self.db.execute(
            "SELECT * FROM budgets WHERE user_id=? AND month=? AND year=?",
            (self.user_id, month, year),
            fetch="one"
        )

        if row is None:
            return Budget(amount=0,totalamount=0, month=month, year=year,  id=None)

        return Budget(
            id=row["id"],
            amount=row["amount"],
            month=row["month"],
            year=row["year"],
            totalamount=row["total_amount"]
        )

    # ----------------------- update budgets after spending -----------------------
    def deduct_from_budget(self, amount_spent: float, month: int, year: int):
        query = "UPDATE budgets SET amount = amount - ? WHERE user_id=? AND month=? AND year=?"
        return self.db.execute(query, (amount_spent, self.user_id, month, year))

    def add_to_budget(self, amount, month, year):
        query = "UPDATE budgets SET amount = amount + ? WHERE user_id=? AND month=? AND year=?"
        return self.db.execute(query, (amount, self.user_id, month, year))

    def increase_budget_total(self, amount, month, year):
        query = """
        UPDATE budgets SET amount = amount + ?, total_amount = total_amount + ?
        WHERE user_id=? AND month=? AND year=?
        """
        return self.db.execute(query, (amount, amount, self.user_id, month, year))

    # ----------------------- return to transaction -----------------------
    def get_budget_balance(self, month, year):
        query = "SELECT amount FROM budgets WHERE user_id = ? AND month = ? AND year = ?"
        return self.db.execute(query, (self.user_id, month, year), fetch="one")

    # ----------------------- future -----------------------
    def get_budget(self, month: int, year: int):
        return self.db.execute(
            "SELECT * FROM budgets WHERE user_id=? AND month=? AND year=?",
            (self.user_id, month, year),
            fetch="one"
        )  
    def update_budget(self, budget_id: int, amount: float):
        query = "UPDATE budgets SET amount = ? WHERE id = ? AND user_id = ?"
        return self.db.execute(query, (amount, budget_id, self.user_id), fetch=None)

    def delete_budget(self, budget_id: int):
        query = "DELETE FROM budgets WHERE id = ? AND user_id = ?"
        return self.db.execute(query, (budget_id, self.user_id), fetch=None)
