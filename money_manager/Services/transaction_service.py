
from repository.transaction_repo import TransactionRepo
from services.ITransactionService import ITransactionService
from models.transaction import Transaction
from services.budget_service import BudgetService


class TransactionService(ITransactionService):
    def __init__(self):
        self.transaction_repo = TransactionRepo()
        self.budget_service = BudgetService()

    def get_budget_warning(self, amount_trans, month, year):
        budget = self.budget_service.check_budget(month, year)
        self.validate_transaction(amount_trans, month, year, budget)

        if budget.totalamount <= 0:
            return None

        remaining_after = budget.amount - amount_trans
        spent_after = budget.totalamount - remaining_after
        spent_percentage = (spent_after / budget.totalamount) * 100

        if spent_percentage >= 80:
            return (
                f"If you continue, you will use {spent_percentage:.1f}% "
                f"of your budget for {month}/{year}.\n"
                "Do you want to continue?"
            )

        return None
   
    # ----------------------- add transaction ------------------------------------------- ----
    def add_transaction(self, amount_trans, category, month, year):
        # Check if budget exists for the month and year
        budget = self.budget_service.check_budget(month, year)
        # Validate transaction against the budget
        self.validate_transaction(amount_trans, month, year, budget)
        # Create and add the transaction
        transaction = Transaction(amount_trans, category, month, year)
        self.transaction_repo.add_transaction(transaction)
        # Deduct the transaction amount from the budget
        self.budget_service.deduct_from_budget(amount_trans, month, year)
        
        return transaction
    
    
    def validate_transaction(self, amount_trans, month, year, budget):
        if abs(amount_trans) <= 0:
            raise ValueError("Amount must be greater than 0")
        if year < 2000 or year > 2100:
            raise ValueError("Year must be between 2000 and 2100")
        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12")
        if budget is None or budget.id is None or budget.totalamount <= 0:
            raise ValueError("No budget found")
        if amount_trans > budget.amount:
            raise ValueError("Amount exceeds the available budget")
    
    def get_budget_balance(self, month, year):
        row = self.budget_service.get_budget_balance(month, year)
        if row:
            return row[0] 
        return 0
    
    def get_transaction_warning(self, old_amount, new_amount):
        diff = new_amount - old_amount

        if diff == 0:
            return None

        if diff > 0:
            impact_text = f"This will increase the amount by {diff}"
        else:
            impact_text = f"This will decrease the amount by {abs(diff)}"

        return f"{impact_text}\nDo you want to continue?"
        
    # ----------------------- ------------------------------------------- ----
    def get_transactions(self):
        return self.transaction_repo.get_transactions()

    def edit_transaction(self, tid, new_amount, month, year):
        if new_amount <= 0:
            return False
        old_transaction = self.transaction_repo.get_transaction_by_id(tid)
        old_amount = old_transaction.amount
        
        difference = new_amount - old_amount  
        self.transaction_repo.update_transaction(tid, new_amount, month, year)

        if difference == 0:
            return True
        if difference > 0:
            self.budget_service.deduct_from_budget(difference, month, year)  
        elif difference < 0:
            self.budget_service.add_to_budget(abs(difference), month, year)
        return True

    def delete_transaction(self, transaction_id):
        transaction = self.transaction_repo.get_transaction_by_id(transaction_id)
        self.transaction_repo.delete_transaction(transaction_id)
        self.budget_service.add_to_budget(transaction.amount, transaction.month, transaction.year)
        
