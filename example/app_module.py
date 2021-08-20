from nest import nest_module
from example.user.module import UserModule
from example.cats.module import CatsModule
from .app_error import AppError


@nest_module(
    prefix='/api/v1',
    modules=[
        CatsModule,
        UserModule
    ],
    ctx=dict(
        hello=lambda: print('hello world from ctx')
    ),
    error_handler=AppError
)
class AppModule:
    pass
