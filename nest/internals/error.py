from nest.scripts.app_context import AppContext
from bottle import HTTPError, request, response
from nest.scripts.types import Types
from inspect import signature


class NestError:
    @staticmethod
    def compile(Err, services: dict):
        if Err is None:
            return None
        injects = NestError.get_meta(Err)
        error = Err(*[services[i] for i in injects])
        error_handler = {}
        for key in error.__dir__():
            route = getattr(error, key)
            if key.startswith('__') or not callable(route) or not hasattr(route, Types.META):
                continue
            http_status = NestError.get_route_meta(route)
            error_handler[http_status] = route
        return {
            'error': error,
            'error_handler': error_handler
        }

    @staticmethod
    def resolve(errors, ctx):
        error_handler = {}
        for status in errors or {}:
            callback = NestError.create_callback(errors[status], ctx)
            error_handler[status] = callback
        return error_handler

    @staticmethod
    def create_callback(fn, ctx):
        def _create_callback(error: HTTPError):
            length = len(signature(fn).parameters)

            if length == 0:
                return fn()

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

        return _create_callback

    @staticmethod
    def get_meta(err):
        meta = getattr(err, Types.META)
        assert meta['type'] == Types.ERROR
        return meta['injects']

    @staticmethod
    def get_route_meta(route):
        meta = getattr(route, Types.META)
        assert meta['type'] == Types.ERROR
        return meta['status']
