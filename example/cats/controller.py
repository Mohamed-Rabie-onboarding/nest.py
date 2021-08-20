from nest import controller, get, post, AppContext
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
    def get_cats_id_handler(self, ctx: AppContext):
        return {
            'id': ctx.params['id'],
            'cats': self.catsService.get_cats()
        }
