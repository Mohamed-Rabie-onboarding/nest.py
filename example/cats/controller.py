from bottle import Request, Response
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

    @Get()
    def get_cats_handler(self, req: Request, res: Response):
        return {
            'cats': self.catsService.get_cats()
        }

    @Post()
    def add_cat_handler(self, req, res):
        return {
            'cats': self.catsService.get_cats()
        }

    @Get('/<id:int>')
    def get_cats_id_handler(self, req, res, id: int):
        return {
            'id': id,
            'cats': self.catsService.get_cats()
        }
