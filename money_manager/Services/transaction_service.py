from data.repositories.transaction_repo import TransactionRepo

class TransactionService:
    def __init__(self, transaction_repo: TransactionRepo):
        self.transaction_repo = transaction_repo

    def add_transaction(self, user_id, name, amount, type_, category):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        return self.transaction_repo.create_transaction(
            user_id, name, amount, type_, category
        )

    def get_user_transactions(self, user_id):
        return self.transaction_repo.get_transactions_by_user(user_id)