from nest.scripts import Types


def nest_error(injects: list = None):
    def _nest_error(Ctor):

        setattr(
            Ctor,
            Types.META,
            dict(
                type=Types.ERROR,
                injects=injects if type(injects) is list else []
            )
        )

        return Ctor

    return _nest_error
