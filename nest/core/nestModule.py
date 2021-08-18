from nest.scripts import Types


def NestModule(prefix: str = None, modules: list = None, providers: list = None, controllers: list = None):
    def _nestModule(Ctor):

        setattr(
            Ctor,
            Types.META,
            dict(
                type=Types.MODULE,
                prefix=prefix if type(prefix) is str else '',
                modules=modules if type(modules) is list else [],
                providers=providers if type(providers) is list else [],
                controllers=controllers if type(controllers) is list else []
            )
        )

        return Ctor

    return _nestModule
