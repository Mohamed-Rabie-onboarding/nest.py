from nest import *
from .service import UserService
from .controller import UserController


@NestModule(
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
