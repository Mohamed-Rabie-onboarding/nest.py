from nest import *
from typing import List
from .model import UserModel


@Injectable()
class UserService:
    users: List[UserModel] = []

    def get_users(self):
        return self.users

    def add_user(self, user: UserModel):
        self.users.append(user)

    def remove_user(self, user: UserModel):
        self.users.remove(user)
