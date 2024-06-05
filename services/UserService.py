from models.User import User


class UserService:
    _users = {}

    @classmethod
    def add_user(cls, username:str):
        user = User(username)
        cls._users[user.id] = user
        return user