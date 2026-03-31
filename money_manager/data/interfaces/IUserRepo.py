from abc import ABC, abstractmethod

class IUserRepo(ABC):

    @abstractmethod
    def find_user(self, user_id: int):
        pass

