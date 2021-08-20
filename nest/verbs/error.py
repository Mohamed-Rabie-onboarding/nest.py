from nest.scripts.types import Types


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
