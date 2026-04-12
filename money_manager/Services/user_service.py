
from repository.user_repo import UserRepo
from services.IUserService import IUserService

class UserService(IUserService):
    def __init__(self, user_repo=None):
        self.user_repo = user_repo or UserRepo()
        self.login_attempts = 0
        self.max_attempts = 4

    def login(self, username, password):
        username = username.strip().lower()
        password = password.strip()
        user = self.user_repo.find_user(username, password)
        if user:
            self.login_attempts = 0
            return user 
        else:
            self.login_attempts += 1
            if self.login_attempts >= self.max_attempts:
                raise Exception("Too many login attempts! Account locked.")
            return None