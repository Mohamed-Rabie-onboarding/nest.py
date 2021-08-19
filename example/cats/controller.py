from nest import controller, get, post
from .service import CatsService


@controller(
    injects=[
        CatsService
    ]
)
class CatsController:

    def __init__(self, catsService: CatsService):
        self.catsService = catsService

    @get()
    def get_cats_handler(self):
        return {
            'cats': self.catsService.get_cats()
        }

    @post()
    def add_cat_handler(self):
        return {
            'cats': self.catsService.get_cats()
        }

    @get('/<id:int>')
    def get_cats_id_handler(self, id: int):
        return {
            'id': id,
            'cats': self.catsService.get_cats()
        }
