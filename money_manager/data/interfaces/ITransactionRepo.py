from abc import ABC, abstractmethod

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