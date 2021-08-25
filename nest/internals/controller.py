from nest.verbs.type_to_verb import type_to_verb
from nest.scripts.types import Types


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
            if not hasattr(routes, r_uri):
                routes[r_uri] = {}
            routes[r_uri][r_method] = route
        return {
            "uri": uri,
            "controller": ctrl,
            "paths": routes
        }

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
