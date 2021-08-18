from nest.scripts.types import Types


class NestFactory:

    @staticmethod
    def create(appModule):
        meta = getattr(appModule, Types.META)
        assert meta['type'] == Types.MODULE

    @staticmethod
    def resolve_module(module):
        meta = getattr(module, Types.META)
        assert meta['type'] == Types.MODULE

        prefix = meta['prefix']
        modules = meta['modules']
        providers = meta['providers']
        controllers = meta['controllers']

    @staticmethod
    def resolve_providers(provider):
        meta = getattr(provider, Types.META)
        assert meta['type'] == Types.INJECTABLE

        injects = meta['injects']

    @staticmethod
    def resolve_controller(controller):
        meta = getattr(controller, Types.META)
        assert meta['type'] == Types.CONTROLLER

        prefix = meta['prefix']
        injects = meta['injects']
