from nest import *
from .service import CatsService


@Controller(
    injects=[
        CatsService
    ]
)
class CatsController:

    def __init__(self, catsService: CatsService):
        self.catsService = catsService

    @Get('/all')
    def get_cats_handler(self):
        return {
            'cats': self.catsService.get_cats()
        }
