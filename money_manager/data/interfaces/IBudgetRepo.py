from abc import ABC, abstractmethod

class IBudgetRepo(ABC):

    @abstractmethod
    def create_budget(self, amount: float, month: int, year: int):
        pass

    @abstractmethod
    def check_budget(self, month: int, year: int):
        pass
    
    @abstractmethod
    def deduct_from_budget(self, amount_spent: float, month: int, year: int):
        pass
    
    @abstractmethod
    def get_budget_balance(self, month: int, year: int):
        pass
    
    @abstractmethod
    def add_to_budget(self, amount, month, year):
        pass
            
    # ----------------------- future -----------------------
    @abstractmethod
    def get_budget(self, month: int, year: int):
        pass

    @abstractmethod
    def update_budget(self, budget_id: int, amount: float):
        pass

    @abstractmethod
    def delete_budget(self, budget_id: int):
        pass