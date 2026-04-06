from data.database import DatabaseConnection
from data.interfaces.IUserRepo import IUserRepo


class UserRepo(IUserRepo):

    def __init__(self):
        pass
        
    def find_user(self, username: str, password: str):
        query = "SELECT * FROM Users WHERE Username = ? AND Password = ?;"
        params = (username, password)


        with DatabaseConnection() as db:
            result  = db.execute(query, params, fetch="one")
        if not result:
            return None
    
        return {
            "id": result[0],
            "username": result[1],
            "permissions": result[2]
        }