from nest.verbs.type_to_verb import type_to_verb
from nest.scripts import Types, register_app_routes, create_error_handlers, install_plugins, merge_apps, compile
from bottle import Bottle


class NestFactory:
    """
    Docs Here!
    """

    @staticmethod
    def create(appModule):
        """
        Docs Here!
        """
        # print(compile(appModule))
        factory = NestFactory(appModule)
        return factory

    def __init__(self, appModule) -> None:
        """
        Docs Here!
        """
        self.app_module = appModule
        self.SERVICES_CONTAINER = {}
        self.app = self.__resolve_module(appModule)

    def use(self, nest_plugin):
        if nest_plugin is None:
            raise TypeError(
                f'`nest_plugin` cannot be of `None` type in `app.use` function'
            )

        return nest_plugin(self.app, self.app_module)

    def listen(
        self,
        port=8080,
        reloader=False,
        debug=None,
        interval=1,
        server='wsgiref',
        host='127.0.0.1',
        quiet=False,
        plugins=None,
        **kargs
    ) -> None:
        """
        Docs Here!
        """
        return self.app.run(
            server=server,
            host=host,
            port=port,
            interval=interval,
            reloader=reloader,
            quiet=quiet,
            plugins=plugins,
            debug=debug,
            **kargs
        )

    def __resolve_module(
        self,
        module,
        ctx=None,
        error_handler=None,
        parent_plugins=[]
    ) -> Bottle:
        """
        Docs Here!
        """

        # Check if the passed value is module with nest_meta
        meta = getattr(module, Types.META)
        assert meta['type'] == Types.MODULE

        # Extract module meta
        prefix = meta['prefix']
        modules = meta['modules']
        providers = meta['providers']
        controllers = meta['controllers']
        error = meta['error']
        context = meta['ctx'] or ctx
        plugins = meta['plugins'] if meta['plugins'] else parent_plugins

        # Create a Bottle app for each module
        main_app = Bottle()

        # Register providers in self.SERVICES_CONTAINER
        self.__resolve_providers(providers)

        # Register each route after resolving them
        routes = [self.__resolve_controller(c) for c in controllers]
        register_app_routes(prefix, main_app, routes, context)

        # Resolve error_handler and register it in main app
        __errors = self.__resolve_error(error) or error_handler
        _error_handler = create_error_handlers(__errors, context)
        main_app.error_handler = _error_handler

        # Register plugins
        install_plugins(main_app, plugins)

        # Resolve all sub modules
        apps = [
            self.__resolve_module(m, context, _error_handler, plugins)
            for m in modules
        ]

        # Checks if there is one app or more it creates a routes_app
        # and merge every sub app into the routes_app so it gives the
        # abillity to mount all apps in a single global prefix
        if len(apps) > 0:
            main_app_routes = merge_apps(apps)
            main_app_routes.error_handler = _error_handler
            install_plugins(main_app_routes, plugins)
            main_app.mount(prefix, main_app_routes)

        return main_app

    def __resolve_providers(self, providers: list):
        """
        Docs Here!
        """
        services = []

        for injectable in providers:
            if injectable in self.SERVICES_CONTAINER:
                services.append(self.SERVICES_CONTAINER[injectable])
                continue

            services.append(self.__resolve_provider(injectable))

        return services

    def __resolve_provider(self, Provider):
        """
        Docs Here!
        """
        meta = getattr(Provider, Types.META)
        assert meta['type'] == Types.INJECTABLE

        injects = meta['injects']
        service = Provider(*self.__resolve_providers(injects))
        self.SERVICES_CONTAINER[Provider] = service

        return service

    def __resolve_controller(self, Controller):
        """
        Docs Here!
        """
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

    def __resolve_error(self, error):
        """
        Docs Here!
        """
        if error is None:
            return None

        meta = getattr(error, Types.META)
        injects = meta['injects']
        services = []

        for inject in injects:
            if inject not in self.SERVICES_CONTAINER:
                raise Exception(f'Service `{inject.__class__}` not found.')
            services.append(self.SERVICES_CONTAINER[inject])

        instance = error(*services)
        error_handler = {}

        for r in instance.__dir__():
            if r.startswith('__'):
                continue

            fn = getattr(instance, r)
            if callable(fn) and hasattr(fn, Types.META):
                error_meta = getattr(fn, Types.META)
                status = error_meta['status']

                if status in error_handler:
                    raise Exception(
                        f'Cannot register multi error handlers with same status_code ({status})')

                error_handler[status] = fn

        return error_handler
