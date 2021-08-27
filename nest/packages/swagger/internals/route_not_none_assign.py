from .types import type_to_key


def route_not_none_assign(configs, route):
    def _route_not_none_assign(t: str):
        if hasattr(route, t):
            configs[type_to_key(t)] = getattr(route, t)
    return _route_not_none_assign
