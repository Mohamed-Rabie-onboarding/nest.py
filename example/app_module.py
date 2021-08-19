from nest import nest_module
from example.user.module import UserModule
from example.cats.module import CatsModule


@nest_module(
    prefix='/api/v1',
    modules=[
        CatsModule,
        UserModule
    ]
)
class AppModule:
    pass
