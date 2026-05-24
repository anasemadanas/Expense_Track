from abc import ABC, abstractmethod


class IUserService(ABC):

    @abstractmethod
    def login(self, username, password):
        pass