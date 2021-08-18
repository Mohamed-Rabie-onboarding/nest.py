from nest.scripts.types import Types


def Get(uri: str = None):
    def _get(fn):

        setattr(
            fn,
            Types.META,
            dict(
                type=Types.GET,
                route=fn,
                uri=uri if uri is str else '/'
            )
        )

        return fn
    return _get
