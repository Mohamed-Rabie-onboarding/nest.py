from nest.scripts.app_context import AppContext
from bottle import Bottle, request, response
from nest.verbs.type_to_verb import type_to_verb
from nest.scripts.types import Types
from inspect import signature


class Controller:
    @staticmethod
    def compile(ctrl, services: dict) -> None:
        uri, injects = Controller.get_meta(ctrl)
        ctrl = ctrl(*[services[i] for i in injects])
        routes = {}
        for key in ctrl.__dir__():
            route = getattr(ctrl, key)
            if key.startswith('__') or not callable(route) or not hasattr(route, Types.META):
                continue
            r_uri, r_method = Controller.get_route_meta(route)
            if not r_uri in routes:
                routes[r_uri] = {}
            routes[r_uri][r_method] = route
        return {
            "uri": uri,
            "controller": ctrl,
            "paths": routes
        }

    @staticmethod
    def resolve(app: Bottle, prefix: str, ctrl, ctx):
        uri, _, paths = Controller.get_ctrl_meta(ctrl)
        for path in paths:
            routes = paths[path]
            for method in routes:
                callback = Controller.create_callback(routes[method], ctx)
                app.route(f'{prefix}{uri}{path}', method, callback)

    @staticmethod
    def create_callback(route, context):
        def _create_callback(*args, **kwargs):
            length = len(signature(route).parameters)

            if length == 0:
                return route()

            return route(
                AppContext(
                    req=request,
                    res=response,
                    params=kwargs,
                    query=request.query,
                    ctx=context
                )
            )
        return _create_callback

    @staticmethod
    def get_meta(ctrl):
        meta = getattr(ctrl, Types.META)
        assert meta['type'] == Types.CONTROLLER
        return (
            meta['prefix'],
            meta['injects'],
        )

    @staticmethod
    def get_route_meta(route):
        meta = getattr(route, Types.META)
        method = type_to_verb(meta['type'])
        uri = meta['uri']
        return (uri, method)

    @staticmethod
    def get_ctrl_meta(ctrl):
        return (
            ctrl['uri'],
            ctrl['controller'],
            ctrl['paths']
        )
