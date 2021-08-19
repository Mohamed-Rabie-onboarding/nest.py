from nest import nest_module
from .service import UserService
from .controller import UserController


@nest_module(
    prefix='/user',
    providers=[
        UserService
    ],
    controllers=[
        UserController
    ]
)
class UserModule:
    pass
