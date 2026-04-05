from data.database import DatabaseConnection
from data.interfaces.IUserRepo import IUserRepo

class UserRepo(IUserRepo):

    def __init__(self):
        pass
        
    def find_user(self, username: str, password: str):
        query = "SELECT * FROM Users WHERE Username = ? AND Password = ?;"
        params = (username, password)

        with DatabaseConnection() as db:
            result = db.execute(query, params, fetch="one")
        return result is not None