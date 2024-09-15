from models.User.User import User
from models.User.UserEntityManager import UserEntityManager
from database.Connection import Connection
import transaction
from faker import Faker

faker = Faker()
if __name__ == "__main__":
    connection = Connection("mydata.fs")
    user_manager = UserEntityManager()
    for i in range(1, 100):
        identifier = f'{faker.random_int(min=1, max=9)}-{faker.random_int(min=1000, max=9999)}-{faker.random_int(min=1000, max=9999)}'
        user = User(identifier, faker.name(), faker.email(), str(faker.random_int(min=18, max=100)))
        user_manager.add_user(user, user.identifier, connection)
    user_manager.read_all_users(connection)
    connection.close()
