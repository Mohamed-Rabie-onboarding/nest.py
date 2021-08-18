from nest import *
from .service import CatsService
from .controller import CatsController


@NestModule(
    prefix="/cats",
    providers=[
        CatsService
    ],
    controllers=[
        CatsController
    ]
)
class CatsModule:
    pass
