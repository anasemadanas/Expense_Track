from abc import ABC, abstractmethod

class IUserRepo(ABC):

    @abstractmethod
    def find_user(self, username: str, password: str):
        pass
