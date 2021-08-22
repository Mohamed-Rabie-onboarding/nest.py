from nest.verbs.type_to_verb import type_to_verb
from nest.scripts.types import Types


def compile(mo, services: dict = {}):
    uri, providers, ctrls, mos, error, ctx, plugins = __get_module_meta(mo)
    for provider in providers:
        __compile_provider(provider, services)
    return {
        "uri": uri,
        "services": services,
        "modules": [compile(m, services) for m in mos],
        "controllers": [__compile_controllers(ctrl, services) for ctrl in ctrls],
        "plugins": plugins,
        "ctx": ctx,
        "error": __compile_error(error, services)
    }


def __compile_provider(Provider, services: dict) -> None:
    if services.get(Provider) is not None:
        return None
    injects = __get_provider_meta(Provider)
    service = Provider(*[__compile_provider(i, services) for i in injects])
    services[Provider] = service
    return None


def __compile_controllers(Controller, services: dict) -> None:
    uri, injects = __get_controller_meta(Controller)
    ctrl = Controller(*[services[i] for i in injects])
    routes = {}
    for key in ctrl.__dir__():
        route = getattr(ctrl, key)
        if __is_not_nest_route(key, route):
            continue
        r_uri, r_method = __get_route_meta(route)
        if not hasattr(routes, r_uri):
            routes[r_uri] = {}
        routes[r_uri][r_method] = route
    return {
        "uri": uri,
        "paths": routes
    }


def __compile_error(Err, services: dict):
    if Err is None:
        return None
    injects = __get_error_meta(Err)
    error = Err(*[services[i] for i in injects])
    error_handler = {}
    for key in error.__dir__():
        route = getattr(error, key)
        if __is_not_nest_route(key, route):
            continue
        http_status = __get_error_route_meta(route)
        error_handler[http_status] = route
    return {
        'error': error,
        'error_handler': error_handler
    }


def __get_module_meta(mo):
    meta = getattr(mo, Types.META)
    assert meta['type'] == Types.MODULE
    return (
        meta['prefix'],
        meta['providers'],
        meta['controllers'],
        meta['modules'],
        meta['error'],
        meta['ctx'],
        meta['plugins']
    )


def __get_provider_meta(provider):
    meta = getattr(provider, Types.META)
    assert meta['type'] == Types.INJECTABLE
    return meta['injects']


def __get_controller_meta(ctrl):
    meta = getattr(ctrl, Types.META)
    assert meta['type'] == Types.CONTROLLER
    return (
        meta['prefix'],
        meta['injects'],
    )


def __get_route_meta(route):
    meta = getattr(route, Types.META)
    method = type_to_verb(meta['type'])
    uri = meta['uri']
    return (uri, method)


def __get_error_meta(err):
    meta = getattr(err, Types.META)
    assert meta['type'] == Types.ERROR
    return meta['injects']


def __get_error_route_meta(route):
    meta = getattr(route, Types.META)
    assert meta['type'] == Types.ERROR
    return meta['status']


def __is_not_nest_route(key, route):
    return key.startswith('__') or not callable(route) or not hasattr(route, Types.META)
