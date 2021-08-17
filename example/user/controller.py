from nest import *
from .service import UserService


@Controller(
    injects=[
        UserService
    ]
)
class UserController:

    def __init__(self, userService: UserService):
        self.userService = userService

    @Get()
    def get_users_handler(self):
        return self.userService.get_users()
