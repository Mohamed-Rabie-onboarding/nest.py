from bottle import Bottle
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
    def resolve(tree, context=None, error_routes=None, parent_plugins=[]):
        """Extract metadata"""
        meta = Module.get_tree_meta(tree)
        uri, _, modules, controllers, plugins, ctx, error = meta
        _ctx = ctx if ctx is not None else context
        _plugins = plugins if type(plugins) is list else parent_plugins

        _error = NestError.resolve(
            error['error_handler'], ctx
        ) if error is not None else error_routes

        """Create Bottle App for each module"""
        app = Bottle()
        """Install plugins for main module"""
        Module.install(app, _plugins)
        app.error_handler = _error
        """Register Main module controllers"""
        [Controller.resolve(app, uri, ctrl, _ctx) for ctrl in controllers]
        """Resolve sub modules"""
        apps = [Module.resolve(mo, _ctx, _error, _plugins) for mo in modules]
        if len(apps) == 0:
            return app

        """If apps length > 0 merge all in a single app"""
        app_routes = Bottle()
        Module.install(app_routes, _plugins)
        app_routes.error_handler = _error
        [app_routes.merge(_app) for _app in apps]
        """Mount using main app"""
        app.mount(uri, app_routes)
        return app

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

    @staticmethod
    def get_tree_meta(tree):
        return (
            tree['uri'],
            tree['services'],
            tree['modules'],
            tree['controllers'],
            tree['plugins'],
            tree['ctx'],
            tree['error']
        )

    @staticmethod
    def install(app: Bottle, plugins: list):
        for plugin in plugins:
            app.install(plugin)
