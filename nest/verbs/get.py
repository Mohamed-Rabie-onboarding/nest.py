from nest.scripts.types import Types


def Get(uri: str = None):
    def _get(fn):

        def NEST_Get(*args, **kwargs):
            return fn(*args, **kwargs)

        setattr(
            NEST_Get,
            Types.meta,
            dict(
                type=Types.get,
                route=fn,
                uri=uri if uri is str else '/'
            )
        )

        return NEST_Get
    return _get
