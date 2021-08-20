from nest import controller, get, post, AppContext
from .service import CatsService

# importing from Bottle for now
from bottle import abort


@controller(
    injects=[
        CatsService
    ]
)
class CatsController:

    def __init__(self, catsService: CatsService):
        self.catsService = catsService

    @get()
    def get_cats_handler(self, ctx: AppContext):
        ctx.ctx['hello']()
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
        id = ctx.params['id']

        if id == 0:
            abort(403, 'No one can access cat of 0 cause its mine!!')

        return {
            'id': ctx.params['id'],
            'cats': self.catsService.get_cats()
        }
