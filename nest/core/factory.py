from nest.verbs.type_to_verb import type_to_verb
from nest.scripts import Types, AppContext, create_error_callback
from bottle import Bottle, request, response
from inspect import signature


class NestFactory:

    def __init__(self, appModule):
        self.SERVICES_CONTAINER = {}
        self.app = self.__resolve_module(appModule)

    def listen(
        self, port=8080, reloader=False, debug=None, interval=1, server='wsgiref', host='127.0.0.1',
            quiet=False, plugins=None, **kargs
    ):
        return self.app.run(
            server=server, host=host, port=port, interval=interval, reloader=reloader,
            quiet=quiet, plugins=plugins, debug=debug, **kargs
        )

    @staticmethod
    def create(appModule):
        factory = NestFactory(appModule)
        return factory

    @staticmethod
    def create_callback(fn, ctx):
        def _callback(*args, **kwargs):

            _len = len(signature(fn).parameters)
            if _len == 1:
                return fn(
                    AppContext(
                        req=request,
                        res=response,
                        params=kwargs,
                        query=request.query,
                        ctx=ctx
                    )
                )

            if _len == 0:
                return fn()

            raise Exception(f'Excepted 0 or 1 parameters but found {_len}')

        return _callback

    def __resolve_module(self, module, ctx=None, error_handler=None):
        meta = getattr(module, Types.META)
        assert meta['type'] == Types.MODULE

        prefix = meta['prefix']
        modules = meta['modules']
        providers = meta['providers']
        controllers = meta['controllers']
        error = meta['error']
        context = meta['ctx'] or ctx

        """
        Created new Bottle app to mount resolved apps
        TODO: add Bottle app configs to module meta.
        """
        main_app = Bottle()

        """
        Resolve all services
        """
        self.__resolve_providers(providers)

        """
        Resolve all controllers
        """

        routes = [self.__resolve_controller(c) for c in controllers]
        for route in routes:
            for uri, methods in route.items():
                for verb, callback in methods.items():

                    main_app.route(
                        prefix + uri,
                        verb,
                        NestFactory.create_callback(
                            callback, context
                        )
                    )

        """
        Resolve error handlers
        """
        __error_handler = self.__resolve_error(error) or error_handler
        _error_handler = {}

        if __error_handler is not None:
            for http_status, error_callback in __error_handler.items():
                _error_handler[http_status] = create_error_callback(
                    error_callback, context
                )

            main_app.error_handler = _error_handler

        """
        Resolve all children modules
        """
        apps = [
            self.__resolve_module(m, context, _error_handler)
            for m in modules
        ]

        if len(apps) > 0:
            main_app_routes = Bottle()
            main_app_routes.error_handler = _error_handler

            for app in apps:
                main_app_routes.merge(app)

            main_app.mount(prefix, main_app_routes)

        return main_app

    def __resolve_providers(self, providers: list) -> None:
        services = []

        for injectable in providers:
            if injectable in self.SERVICES_CONTAINER:
                services.append(self.SERVICES_CONTAINER[injectable])
                continue

            services.append(self.__resolve_provider(injectable))

        return services

    def __resolve_provider(self, Provider):
        meta = getattr(Provider, Types.META)
        assert meta['type'] == Types.INJECTABLE

        injects = meta['injects']
        service = Provider(*self.__resolve_providers(injects))
        self.SERVICES_CONTAINER[Provider] = service

        return service

    # , global_prefix=''
    def __resolve_controller(self, Controller):
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

    def __resolve_error(self, error):
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
