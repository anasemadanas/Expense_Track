from abc import ABC, abstractmethod


class ITransactionService(ABC):

    @abstractmethod
    def get_budget_warning(self, amount_trans, month, year):
        pass

    @abstractmethod
    def add_transaction(self, amount_trans, category, month, year):
        pass

    @abstractmethod
    def validate_transaction(self, amount_trans, month, year, budget):
        pass

    @abstractmethod
    def get_budget_balance(self, month, year):
        pass

    @abstractmethod
    def get_transactions(self):
        pass

    @abstractmethod
    def edit_transaction(self, tid, new_amount, month, year):
        pass

    @abstractmethod
    def delete_transaction(self, transaction_id):
        pass
