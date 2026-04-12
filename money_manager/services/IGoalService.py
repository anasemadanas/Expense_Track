from abc import ABC, abstractmethod


class IGoalService(ABC):

    @abstractmethod
    def add_goal(self, name: str, target_amount: float, initial_saved: float = 0.0):
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