from nest import controller, get, post, AppContext
from .service import CatsService
from nest.packages.swagger import api_description, api_summary, api_response, api_tags, api_parameter, Model, ModelType

# importing from Bottle for now
from bottle import HTTPError, abort


@controller(
    injects=[
        CatsService
    ]
)
class CatsController:

    def __init__(self, catsService: CatsService):
        self.catsService = catsService

    @get()
    @api_description('Hello world')
    @api_summary('summary!!')
    @api_tags(['Cat'])
    @api_response(200, 'its OK!', 'Order')
    def get_cats_handler(self, ctx: AppContext):
        ctx.ctx['hello']()
        return {
            'cats': self.catsService.get_cats()
        }

    @post()
    @api_response(400, 'Bad Request')
    def add_cat_handler(self, ctx: AppContext):
        return self.catsService.add_cat(ctx.req.json['name'])

    @get('/<id:int>')
    @api_parameter('id', 'path', 'awesome', True, 1)
    @api_response(500, 'Internal server error')
    def get_cats_id_handler(self, ctx: AppContext):
        id = ctx.params['id']

        if id == 0:
            abort(403, 'No one can access cat of 0 cause its mine!!')

        if id == 100:
            raise HTTPError(404, 'Cat not found')

        return {
            'id': ctx.params['id'],
            'cats': self.catsService.get_cats()
        }
