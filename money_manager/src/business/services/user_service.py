from src.data.repositories.user_repo import UserRepo
from src.shared.utils import hash_password

class UserService:
    def __init__(self, user_repo: UserRepo):
        self.user_repo = user_repo

    def register_user(self, username: str, password: str, email: str, phone: str = None):
        hashed = hash_password(password)
        return self.user_repo.create_user(username, hashed, email, phone)

    def login_user(self, username: str, password: str):
        hashed = hash_password(password)
        user = self.user_repo.get_user_by_username(username)
        if user and user['Password'] == hashed:
            return user
        return None

    def get_user(self, user_id: int):
        return self.user_repo.get_user_by_id(user_id)