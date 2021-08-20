from bottle import Bottle
from .app_context import AppContext
from .create_route_callback import create_route_callback


def register_app_routes(prefix: str, app: Bottle, routes: list, ctx: AppContext) -> None:
    for route in routes:
        for uri, methods in route.items():
            for verb, callback in methods.items():
                app.route(
                    prefix + uri,
                    verb,
                    create_route_callback(callback, ctx)
                )
