from nest import nest_error, error, AppContext
from json import dumps


@nest_error()
class AppError:

    @error(404)
    def error_404_handler(self, ctx: AppContext):
        ctx.res.set_header('content-type', 'application/json')
        ctx.res.status = 404

        return dumps({
            'status': 404,
            'error': True,
            'message': ctx.error.body
        })

    @error(500)
    def error_500_handler(self, ctx: AppContext):
        ctx.res.set_header('content-type', 'application/json')
        ctx.res.status = 500

        return dumps({
            'status': 500,
            'error': True,
            'message': 'Internal server error.'
        })
