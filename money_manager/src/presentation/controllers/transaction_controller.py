from ...business.services.transaction_service import TransactionService

class TransactionController:
    def __init__(self):
        self.service = TransactionService()

    def add_transaction(self, name: str, amount: float, category: str, trans_type: str, user_id: int):

        return self.service.create_transaction(
            name=name,
            amount=amount,
            category=category,
            trans_type=trans_type,
            user_id=user_id
        )

    def get_transactions_by_user(self, user_id: int):

        return self.service.get_transactions(user_id=user_id)

    def update_transaction(self, transaction_id: int, **kwargs):

        return self.service.update_transaction(transaction_id, **kwargs)

    def delete_transaction(self, transaction_id: int):

        return self.service.delete_transaction(transaction_id)