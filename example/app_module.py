from nest import nest_module
from example.user.module import UserModule
from example.cats.module import CatsModule
from .app_error import AppError


def test(cb):
    def w(*args, **kwargs):
        print(args, kwargs)
        print('here?')
        return cb(*args, **kwargs)

    return w


@nest_module(
    prefix='/api/v1',
    modules=[
        CatsModule,
        UserModule
    ],
    ctx=dict(
        hello=lambda: print('hello world from ctx')
    ),
    error_handler=AppError,
    plugins=[test]
)
class AppModule:
    pass
