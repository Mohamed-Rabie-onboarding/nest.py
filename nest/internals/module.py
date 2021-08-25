from nest.scripts.types import Types

from .provider import Provider
from .controller import Controller
from .error import NestError


class Module:

    @staticmethod
    def compile(module, services: dict = {}):
        meta = Module.get_meta(module)
        uri, providers, ctrls, modules, error, ctx, plugins = meta

        for provider in providers:
            Provider.compile(provider, services)

        return {
            "uri": uri,
            "services": services,
            "modules": [Module.compile(mo, services) for mo in modules],
            "controllers": [Controller.compile(ctrl, services) for ctrl in ctrls],
            "plugins": plugins,
            "ctx": ctx,
            "error": NestError.compile(error, services)
        }

    @staticmethod
    def get_meta(module):
        meta = getattr(module, Types.META)
        assert meta['type'] == Types.MODULE
        return (
            meta['prefix'],
            meta['providers'],
            meta['controllers'],
            meta['modules'],
            meta['error'],
            meta['ctx'],
            meta['plugins']
        )
