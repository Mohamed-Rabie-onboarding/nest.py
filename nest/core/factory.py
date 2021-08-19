from nest.verbs import type_to_verb
from nest.scripts import Types
from bottle import Bottle, request, response


class NestFactory:

    """
    Should change this way 100%
    """

    def __init__(self, appModule):
        self.SERVICES_CONTAINER = {}
        self.app = self.resolve_module(appModule)

    @staticmethod
    def create(appModule):
        factory = NestFactory(appModule)
        return factory.app

    @staticmethod
    def create_callback(fn):
        def _callback(*args, **kwargs):
            # can add req, req here
            return fn(*args, **kwargs)
        return _callback

    def resolve_module(self, module):
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
        self.resolve_providers(providers)

        """
        Resolve all controllers
        """

        routes = [self.resolve_controller(c) for c in controllers]
        for route in routes:
            for uri, methods in route.items():
                for verb, callback in methods.items():

                    main_app.route(
                        prefix + uri,
                        verb,
                        NestFactory.create_callback(callback)
                    )

        """
        Resolve all children modules
        """
        apps = [self.resolve_module(m) for m in modules]

        if len(apps) > 0:
            main_app_routes = Bottle()

            for app in apps:
                main_app_routes.merge(app)

            main_app.mount(prefix, main_app_routes)

        return main_app

    def resolve_providers(self, providers: list) -> None:
        services = []

        for injectable in providers:
            if injectable in self.SERVICES_CONTAINER:
                services.append(self.SERVICES_CONTAINER[injectable])
                continue

            services.append(self.resolve_provider(injectable))

        return services

    def resolve_provider(self, Provider):
        meta = getattr(Provider, Types.META)
        assert meta['type'] == Types.INJECTABLE

        injects = meta['injects']
        service = Provider(*self.resolve_providers(injects))
        self.SERVICES_CONTAINER[Provider] = service

        return service

    # , global_prefix=''
    def resolve_controller(self, Controller):
        meta = getattr(Controller, Types.META)
        assert meta['type'] == Types.CONTROLLER

        prefix = meta['prefix']
        injects = meta['injects']
        services = []

        for inject in injects:
            if inject not in self.SERVICES_CONTAINER:
                raise Exception(f'Service `{inject.__class__}` not found.')
            services.append(self.SERVICES_CONTAINER[inject])

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

                route_type = route_meta['type']
                method = type_to_verb(route_type)
                uri = prefix + route_meta['uri']

                if not uri in routes:
                    routes[uri] = {}

                if method in routes[uri]:
                    raise Exception(
                        'Can\'t Register multi routes with same method and uri.'
                    )

                routes[uri][method] = fn
        return routes
