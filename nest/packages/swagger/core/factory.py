from typing import List
from nest.core.factory import NestFactory
from .info import Info
from .tag import Tag
from .security_definitions import SecurityDefinitions


class SwaggerFactory:

    def setup(self, factory: NestFactory, uri: str = '/api/docs'):
        # register here
        pass

    def __init__(
        self,
        swagger: str = None,
        host: str = None,
        base_path: str = None,
        info: Info = None,
        tags: List[Tag] = None,
        schemes: List[str] = None,
        security_definitions: SecurityDefinitions = None,
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
            'paths': '??',
            'models': '??',
            **kwargs
        }
