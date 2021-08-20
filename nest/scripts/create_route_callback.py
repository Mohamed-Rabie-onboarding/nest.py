from inspect import signature
from .app_context import AppContext
from bottle import response, request
from warnings import warn


def create_route_callback(fn, ctx):

    def _callback(*args, **kwargs):
        if len(args) > 0:
            warn(
                f'Ignored `{len(args)}` unexcepted `Positional Arguments` passed to  `{fn.__name__}` route.'
            )

        _len = len(signature(fn).parameters)
        if _len == 1:
            return fn(
                AppContext(
                    req=request,
                    res=response,
                    params=kwargs,
                    query=request.query,
                    ctx=ctx
                )
            )

        if _len == 0:
            return fn()

        raise Exception(
            f'Excepted `Positional Arguments` of length `0 or 1` but found `{_len}` in `{fn.__name__}` route.'
        )

    return _callback
