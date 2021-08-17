from nest.scripts import Types


def Controller(prefix: str = None, injects: list = None):
    def _controller(Ctor):

        setattr(
            Ctor,
            Types.meta,
            dict(
                type=Types.controller,
                prefix=prefix if type(prefix) is str else '',
                injects=injects if type(injects) is list else [],
            )
        )

        return Ctor
    return _controller
