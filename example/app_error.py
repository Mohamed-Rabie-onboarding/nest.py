from nest import nest_error, error, AppContext
from json import dumps


@nest_error()
class AppError:

    @error(400)
    def error_400_handler(self, ctx: AppContext):
        res = ctx.res
        res.set_header('content-type', 'application/json')

        return dumps({
            'status': 400,
            'message': 'Bad Request.'
        })

    @error(403)
    def error_403_handler(self, ctx: AppContext):
        # res = ctx.res
        # res.set_header('content-type', 'application/json')
        print(ctx.error.body)

        return dumps({
            'status': 403,
            'message': ctx.error.body
        })

    @error(404)
    def error_404_handler(self, ctx: AppContext):
        res = ctx.res
        res.set_header('content-type', 'application/json')

        return dumps({
            'status': 404,
            'message': ctx.error.body
        })

    @error(405)
    def error_405_handler(self):
        return dumps({
            'works?': 'yay!'
        })

    @error(500)
    def error_500_handler(self, ctx: AppContext):
        res = ctx.res
        res.set_header('content-type', 'application/json')

        return dumps({
            'status': 500,
            'message': 'Internal server error.'
        })
