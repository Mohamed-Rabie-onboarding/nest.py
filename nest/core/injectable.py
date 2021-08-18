from nest.scripts import Types


def Injectable(injects: list = None):
    def _injectable(Ctor):

        setattr(
            Ctor,
            Types.META,
            dict(
                type=Types.INJECTABLE,
                injects=injects if type(injects) is list else []
            )
        )

        return Ctor
    return _injectable
