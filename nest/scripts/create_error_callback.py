from bottle import HTTPError, request, response
from .app_context import AppContext


def create_error_callback(fn, ctx):
    def _callback(error: HTTPError):
        print('*' * 50)
        print(error)
        print('*' * 50)

        return fn(
            AppContext(
                req=request,
                res=response,
                ctx=ctx,
                error=error,
                query=None,
                params=None
            )
        )

    return _callback
