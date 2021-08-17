from nest.scripts.types import Types


class NestFactory:

    @staticmethod
    def create(appModule):
        meta = getattr(appModule, Types.meta)
        assert meta['type'] == Types.module

    @staticmethod
    def resolve_module(module):
        meta = getattr(module, Types.meta)
        assert meta['type'] == Types.module

        prefix = meta['prefix']
        modules = meta['modules']
        providers = meta['providers']
        controllers = meta['controllers']

    @staticmethod
    def resolve_providers(provider):
        meta = getattr(provider, Types.meta)
        assert meta['type'] == Types.injectable

        injects = meta['injects']

    @staticmethod
    def resolve_controller(controller):
        meta = getattr(controller, Types.meta)
        assert meta['type'] == Types.controller

        prefix = meta['prefix']
        injects = meta['injects']
