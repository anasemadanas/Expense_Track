from abc import ABC, abstractmethod

class ITransactionRepo(ABC):

    @abstractmethod
    def create_transaction(self, name: str, amount: float, category: str,
                           t_type: str, user_id: int,
                           budget_id: int = None, family_id: int = None,
                           currency_id: int = None):
        pass

    @abstractmethod
    def get_transaction(self, transaction_id: int):
        pass

    @abstractmethod
    def get_transactions_by_user(self, user_id: int):
        pass

    @abstractmethod
    def get_transactions_by_budget(self, budget_id: int):
        pass

    @abstractmethod
    def delete_transaction(self, transaction_id: int):
        pass