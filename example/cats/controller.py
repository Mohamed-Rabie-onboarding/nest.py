from nest import controller, get, post, AppContext, put, delete
from .service import CatsService
from bottle import HTTPError
from nest.packages.swagger import api_response, api_summary, api_tags, api_parameter, api_deprecated


@controller(
    injects=[
        CatsService
    ]
)
class CatsController:

    def __init__(self, catsService: CatsService):
        self.catsService = catsService

    @get()
    @api_tags(['Cat'])
    @api_summary('Returns all cats.')
    @api_response(200, 'Returned back all cats.', schema='Cat[]')
    @api_deprecated(True)
    def get_cats_handler(self):
        return {
            'cats': self.catsService.get_cats()
        }

    @get('/<id:int>')
    @api_tags(['Cat'])
    @api_summary('Returns a cat by id if it exists.')
    @api_parameter('id', 'path', example=1, required=True)
    @api_response(200, 'Found cat and returned it.', schema='Cat')
    @api_response(404, 'Cat not found.')
    def get_cat_by_id_handler(self, ctx: AppContext):
        cat = self.catsService.get_cat_by_id(ctx.params['id'])
        if cat is None:
            raise HTTPError(404, 'Cat not found.')
        return cat

    @post()
    @api_tags(['Cat'])
    @api_summary('Creates a new cat with the given name.')
    @api_parameter('body', 'body', schema='CatInput')
    @api_response(201, 'Cat was created.', schema='Cat')
    def add_cat_handler(self, ctx: AppContext):
        ctx.res.status = 201
        return self.catsService.add_cat(ctx.req.json['name'])

    @put('/<id:int>')
    @api_tags(['Cat'])
    @api_summary('Updates a cat if it exists.')
    @api_parameter('id', 'path', example=1, required=True)
    @api_parameter('body', 'body', schema='CatInput')
    @api_response(202, 'Cat was updated.', schema='Cat')
    @api_response(404, 'Cat was not found.')
    def update_cat_handler(self, ctx: AppContext):
        cat = self.catsService.update_cat(
            ctx.params['id'],
            ctx.req.json['name']
        )
        if cat is None:
            raise HTTPError(404, 'Cat not found.')
        ctx.res.status = 202
        return cat

    @delete('/<id:int>')
    @api_tags(['Cat'])
    @api_summary('Deletes a cat if it exists.')
    @api_response(204, 'Cat was deleted.')
    @api_response(404, 'Cat was not found.')
    def delete_cat_handler(self, ctx: AppContext):
        cat = self.catsService.delete_cat(ctx.params['id'])
        if cat is None:
            raise HTTPError(404, 'Cat not found.')
        ctx.res.status = 204
