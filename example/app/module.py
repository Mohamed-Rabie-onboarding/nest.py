from nest import *
from example.user import UserModule


@NestModule(
    prefix='/api/v1',
    modules=[
        UserModule
    ]
)
class AppModule:
    pass
