from typing import List
from nest.core.factory import NestFactory
from .info import Info
from .tag import Tag
from .security_definitions import SecurityDefinitions
from .definitions import Definitions
from bottle import template, static_file
import os
from json import dumps


class SwaggerFactory:

    def setup(self, factory: NestFactory, uri: str = '/api/docs'):
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
            'paths': '??',
            **kwargs
        }
