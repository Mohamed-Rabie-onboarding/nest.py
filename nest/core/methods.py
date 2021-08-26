from nest.scripts.types import Types


def __create_route(route_type: str):
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


get = __create_route(Types.GET)
post = __create_route(Types.POST)
put = __create_route(Types.PUT)
patch = __create_route(Types.PATCH)
delete = __create_route(Types.DELETE)


def error(http_status: int = 500):
    def _error(fn):

        setattr(
            fn,
            Types.META,
            dict(
                type=Types.ERROR,
                status=http_status
            )
        )

        return fn
    return _error
