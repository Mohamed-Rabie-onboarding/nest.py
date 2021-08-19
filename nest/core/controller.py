from nest.scripts import Types


def controller(prefix: str = None, injects: list = None):
    def _controller(Ctor):

        setattr(
            Ctor,
            Types.META,
            dict(
                type=Types.CONTROLLER,
                prefix=prefix if type(prefix) is str else '',
                injects=injects if type(injects) is list else [],
            )
        )

        return Ctor
    return _controller
