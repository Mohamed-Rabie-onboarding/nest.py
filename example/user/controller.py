from nest import controller, get
from .service import UserService
from nest.packages.swagger import api_property, api_response


@controller(
    prefix='/s',
    injects=[
        UserService
    ]
)
class UserController:

    def __init__(self, userService: UserService):
        self.userService = userService

    @api_property(
        tags=['User'],
        summary="Example User summary",
        description="Example user description",
        responses={
            '200': api_response(
                description="its OK!",
                schema='#User'
            ),
            '400': api_response(
                description="Bad Reqest"
            ),
            "500": api_response(
                description="Internal Server Error!"
            )
        }
    )
    @get()
    def get_users_handler(self):
        return dict(
            users=self.userService.get_users()
        )
