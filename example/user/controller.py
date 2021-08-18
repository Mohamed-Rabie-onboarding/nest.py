from nest import *
from .service import UserService
from bottle import response
from json import dumps


@Controller(
    prefix='/s',
    injects=[
        UserService
    ]
)
class UserController:

    def __init__(self, userService: UserService):
        self.userService = userService

    @Get()
    def get_users_handler(self):
        return dict(
            users=self.userService.get_users()
        )
