from nest import controller, get, post, AppContext, put, delete
from .service import CatsService
from nest.packages.swagger import api_description, api_summary, api_response, api_tags, api_parameter, Model, ModelType
from bottle import HTTPError


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

    @get('/<id:int>')
    def get_cat_by_id_handler(self, ctx: AppContext):
        cat = self.catsService.get_cat_by_id(ctx.params['id'])
        if cat is None:
            raise HTTPError(404, 'Cat not found.')
        return cat

    @post()
    def add_cat_handler(self, ctx: AppContext):
        ctx.res.status = 201
        return self.catsService.add_cat(ctx.req.json['name'])

    @put('/<id:int>')
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
    def delete_cat_handler(self, ctx: AppContext):
        cat = self.catsService.delete_cat(ctx.params['id'])
        if cat is None:
            raise HTTPError(404, 'Cat not found.')
        ctx.res.status = 204
