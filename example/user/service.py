from nest import *
from typing import List
from .model import UserModel


@Injectable()
class UserService:
    users: List[UserModel] = [
        UserModel(0, 'Mohamed'),
        UserModel(1, 'Mohamed'),
        UserModel(2, 'Mohamed'),
        UserModel(3, 'Mohamed'),
        UserModel(4, 'Mohamed'),
    ]

    def get_users(self):
        return [user.to_dict() for user in self.users]
