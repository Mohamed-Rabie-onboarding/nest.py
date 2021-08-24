from nest import controller, get
from .service import UserService
# from nest.packages.swagger import api_property, api_response


@controller(
    prefix='/s',
    injects=[
        UserService
    ]
)
class UserController:

    def __init__(self, userService: UserService):
        self.userService = userService

    # @api_property(
    #     tags=['User'],
    #     summary="Example User summary",
    #     description="Example user description",
    # )
    # @api_response(200, 'its Ok!', 'User')
    # @api_response(400, 'Bad Request')
    # @api_response(500, 'Internal server error.')
    @get()
    def get_users_handler(self):
        return dict(
            users=self.userService.get_users()
        )
