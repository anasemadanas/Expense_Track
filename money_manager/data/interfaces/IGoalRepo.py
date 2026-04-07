from abc import ABC, abstractmethod

class IGoalRepo(ABC):

    @abstractmethod
    def create_goal(self, name: str, target_amount: float):
        pass

    @abstractmethod
    def get_all_goals(self):
        pass

    @abstractmethod
    def add_savings(self, goal_id: int, amount: float):
        pass

    @abstractmethod
    def delete_goal(self, goal_id: int):
        pass
