from nest.verbs import type_to_verb
from nest.scripts import Types
from bottle import Bottle


class NestFactory:

    """
    Should change this way 100%
    """
    SERVICES_CONTAINER = dict()

    @staticmethod
    def create(appModule):
        app = NestFactory.resolve_module(appModule)
        return app

    @staticmethod
    def resolve_module(module):
        meta = getattr(module, Types.META)
        assert meta['type'] == Types.MODULE

        prefix = meta['prefix']
        modules = meta['modules']
        providers = meta['providers']
        controllers = meta['controllers']

        """
        Created new Bottle app to mount resolved apps
        TODO: add Bottle app configs to module meta.
        """
        main_app = Bottle()

        """
        Resolve all services
        """
        NestFactory.resolve_providers(providers)

        """
        Resolve all controllers
        """
        routes = [
            NestFactory.resolve_controller(c, prefix) for c in controllers
        ]
        for route in routes:
            for path in route:
                r = route[path]
                method = r['method']
                callback = r['route']

                main_app.route(path, method, callback)

        """
        Resolve all children modules
        """
        apps = [NestFactory.resolve_module(module) for module in modules]

        if len(apps) > 0:
            main_app_routes = Bottle()

            for app in apps:
                main_app_routes.merge(app)

            main_app.mount(prefix, main_app_routes)

        return main_app

    @staticmethod
    def resolve_providers(providers: list) -> None:
        services = []

        for injectable in providers:
            if injectable in NestFactory.SERVICES_CONTAINER:
                services.append(NestFactory.SERVICES_CONTAINER[injectable])
                continue

            services.append(NestFactory.resolve_provider(injectable))

        return services

    @staticmethod
    def resolve_provider(Provider):
        meta = getattr(Provider, Types.META)
        assert meta['type'] == Types.INJECTABLE

        injects = meta['injects']
        service = Provider(*NestFactory.resolve_providers(injects))
        NestFactory.SERVICES_CONTAINER[Provider] = service

        return service

    @staticmethod
    def resolve_controller(Controller, global_prefix=''):
        meta = getattr(Controller, Types.META)
        assert meta['type'] == Types.CONTROLLER

        prefix = meta['prefix']
        injects = meta['injects']
        services = []

        for inject in injects:
            if inject not in NestFactory.SERVICES_CONTAINER:
                raise Exception(f'Service `{inject.__class__}` not found.')
            services.append(NestFactory.SERVICES_CONTAINER[inject])

        controller = Controller(*services)

        """
        Extract each route from controller
        """
        # routes = [r for r in controller.__dir__() if callable()]
        routes = {}

        for r in controller.__dir__():
            if r.startswith('__'):
                continue

            fn = getattr(controller, r)
            if callable(fn) and hasattr(fn, Types.META):
                route_meta = getattr(fn, Types.META)
                method = type_to_verb(route_meta['type'])

                routes[global_prefix + prefix] = dict(
                    method=method,
                    route=fn
                )

        return routes
