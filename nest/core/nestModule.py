from typing import List
from nest.scripts import Types


def NestModule(config: dict = None):
    def _nestModule(Ctor):
        modules = []
        providers = []
        controllers = []

        if config is dict:
            modules = config.modules if config.modules is List else modules
            providers = config.providers if config.providers is List else providers
            controllers = config.controllers if config.controllers is List else controllers

        class NEST_MODULE(Ctor):
            pass

        setattr(
            NEST_MODULE,
            Types.meta,
            dict(
                type=Types.module,
                module=Ctor,
                modules=modules,
                providers=providers,
                controllers=controllers
            )
        )

        return NEST_MODULE

    return _nestModule
