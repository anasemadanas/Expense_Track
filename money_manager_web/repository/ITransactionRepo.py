from abc import ABC, abstractmethod
from models.transaction import Transaction

class ITransactionRepo(ABC):

    @abstractmethod
    def add_transaction(self, transaction: Transaction):
        pass

    @abstractmethod
    def get_transactions(self):
        pass

    @abstractmethod
    def delete_transaction(self, transaction_id: int):
        pass
    
    @abstractmethod
    def update_transaction(self, transaction_id, new_amount, new_month, new_year):
        pass
    
    @abstractmethod    
    def get_transaction_by_id(self, transaction_id: int):
        pass
    
    @abstractmethod
    def get_transactions_by_month(self, month, year):
        pass