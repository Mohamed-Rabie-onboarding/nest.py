from typing import List
from nest.core.factory import NestFactory
from .info import Info
from .tag import Tag
from .security_definitions import SecurityDefinitions
from .definitions import Definitions
from bottle import template, static_file
import os
from json import dumps
from nest.packages.swagger.internals import Types, route_not_none_assign
import re


class SwaggerFactory:

    def setup(self, factory: NestFactory, uri: str = '/api/docs'):
        paths = SwaggerFactory.__resolve_paths(factory)
        self.configs['paths'] = paths

        index = os.path.join(os.path.dirname(__file__), '..', 'ui')
        static = os.path.join(index, 'static')

        def serve_index():
            spec = dumps(self.configs)
            return template(index + '/index', uri=uri, spec=spec)
        factory.app.get(uri, callback=serve_index)

        def serve_static(filename: str):
            return static_file(filename, static)
        factory.app.get(uri + '/<filename>', callback=serve_static)

    def __init__(
        self,
        swagger: str = None,
        host: str = None,
        base_path: str = None,
        info: Info = None,
        tags: List[Tag] = None,
        schemes: List[str] = None,
        security_definitions: SecurityDefinitions = None,
        definitions: Definitions = None,
        **kwargs
    ):
        self.configs = {
            'swagger': swagger,
            'host': host,
            'basePath': base_path,
            'info': info.configs if isinstance(info, Info) else info,
            'tags': [tag.configs for tag in tags] if type(tags) is list else tags,
            'schemes': schemes,
            'securityDefinitions': security_definitions.configs if isinstance(security_definitions, SecurityDefinitions) else security_definitions,
            'definitions': definitions.configs if isinstance(definitions, Definitions) else definitions,
            **kwargs
        }

    @staticmethod
    def __resolve_paths(factory: NestFactory):
        tree = factory.tree
        paths = SwaggerFactory.__resolve_modules(tree['modules'])
        SwaggerFactory.__resolve_controllers(
            paths,
            tree['uri'],
            tree['controllers']
        )
        return paths

    @staticmethod
    def __resolve_modules(modules, paths: dict = {}, prefix=''):
        for mo in modules:
            uri = prefix + mo['uri']
            SwaggerFactory.__resolve_controllers(paths, uri, mo['controllers'])
            SwaggerFactory.__resolve_modules(mo['modules'], paths, uri)

        return paths

    @staticmethod
    def __resolve_controllers(paths: dict, uri: str, ctrls: list):
        for ctrl in ctrls:
            base_url = uri + ctrl['uri']
            routes = ctrl['paths']
            for route in routes:
                url = SwaggerFactory.__resolve_url(base_url + route)
                paths[url] = {}
                for method in routes[route]:
                    cb = routes[route][method]
                    configs = SwaggerFactory.__get_route_configs(cb)
                    if configs is not None:
                        paths[url][method.lower()] = configs

    @staticmethod
    def __resolve_url(url: str):
        res_url = ''
        for item in re.split(r'(<|>)', url):
            if item == '<' or item == '>':
                continue
            if ':' in item:
                parts = item.split(':')
                res_url += '{' + parts[0] + '}'
                continue
            res_url += item
        return res_url

    @staticmethod
    def __get_route_configs(route):
        configs = {}
        assign_configs = route_not_none_assign(configs, route)
        assign_configs(Types.RESPONSES)
        if 'responses' not in configs:
            return None
        assign_configs(Types.SUMMARY)
        assign_configs(Types.TAGS)
        assign_configs(Types.SCHEMES)
        assign_configs(Types.OPERATION_ID)
        assign_configs(Types.CONSUMES)
        assign_configs(Types.DEPRECATED)
        assign_configs(Types.DESCRIPTION)
        assign_configs(Types.PRODUCES)
        assign_configs(Types.SECURITY)
        assign_configs(Types.EXTERNAL_DOCS)
        assign_configs(Types.PARAMETERS)
        return configs
