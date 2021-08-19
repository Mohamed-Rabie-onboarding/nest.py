from nest import controller, get
from .service import UserService


@controller(
    prefix='/s',
    injects=[
        UserService
    ]
)
class UserController:

    def __init__(self, userService: UserService):
        self.userService = userService

    @get()
    def get_users_handler(self, req, res):
        return dict(
            users=self.userService.get_users()
        )
