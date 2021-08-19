from nest.scripts.types import Types


def create_route(route_type: str):
    def route(uri: str = None):
        def _route(fn):

            setattr(
                fn,
                Types.META,
                dict(
                    type=route_type,
                    uri=uri if type(uri) is str else '',
                )
            )

            return fn
        return _route
    return route
