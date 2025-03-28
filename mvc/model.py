from dataclasses import dataclass
from .storage import get_klanten, insert_klant

@dataclass
class User():
    nr: int
    naam:str

class UserModel():
    def __init__(self):
        self.current_user = None
        self.error = None
    def get_users(self) -> list[User]:
        users = get_klanten()
        return [User(user[0], user[1]) for user in users]
    
    def insert_user(self, user:User):
        self.current_user = None
        self.error = None
        try:
            insert_klant(user.nr, user.naam)
            return user.nr
        except ValueError as e:
            self.current_user = user
            self.error = f"{self.current_user.nr} is al in gebruik"
            raise e