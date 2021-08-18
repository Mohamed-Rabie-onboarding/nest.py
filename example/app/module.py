from nest import *
from example.user import UserModule
from example.cats import CatsModule


@NestModule(
    prefix='/api/v1',
    modules=[
        CatsModule,
        UserModule
    ]
)
class AppModule:
    pass
