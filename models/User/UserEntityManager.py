import transaction
from database.Connection import Connection
from models.User.User import User


class UserEntityManager:
    def __init__(self):
        pass

    def read_all_users(self, connection: Connection):
        for key in connection.root.keys():
            print(connection.root[key])

    def add_user(self, user: User, user_id: str, connection: Connection):
        if user_id in connection.root.keys():
            print("User already exists!")
            return
        connection.root[user_id] = user
        transaction.commit()

    def read_user(self, user_id: str, connection: Connection):
        if user_id not in connection.root.keys():
            print("User does not exist!")
            return
        user = connection.root[user_id]
        print(user)

    def update_user(self, user_id: str, user: User, connection: Connection):
        connection.root[user_id] = user
        transaction.commit()

    def delete_user(self, user_id: str, connection: Connection):
        del connection.root[user_id]
        transaction.commit()
