from nest.scripts import Types


def Injectable(injects: list = None):
    def _injectable(Ctor):

        setattr(
            Ctor,
            Types.meta,
            dict(
                type=Types.injectable,
                injects=injects if type(injects) is list else []
            )
        )

        return Ctor
    return _injectable
