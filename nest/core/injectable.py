from nest.scripts import Types


def Injectable(config: dict = None):
    def _injectable(Ctor):
        injects = []

        if config is dict:
            injects = config.injects if config.injects is not None else injects

        class NEST_Injectable(Ctor):
            pass

        setattr(
            NEST_Injectable,
            Types.meta,
            dict(
                type=Types.injectable,
                injectable=Ctor,
                injects=injects
            )
        )

        return NEST_Injectable
    return _injectable
