from nest import nest_module
from .service import CatsService
from .controller import CatsController


@nest_module(
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
