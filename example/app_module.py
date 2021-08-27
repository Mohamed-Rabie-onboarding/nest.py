from nest import nest_module
from example.cats.module import CatsModule
from .app_error import AppError


@nest_module(
    prefix='/api/v1',
    modules=[
        CatsModule
    ],
    error_handler=AppError
)
class AppModule:
    pass
