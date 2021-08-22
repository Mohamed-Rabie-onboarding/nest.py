from nest.scripts.types import Types
from bottle import Bottle


class SwaggerFactory:

    @staticmethod
    def create(
        title: str = None,
        description: str = None,
        version: str = None,
        base_path: str = None,
        security_definitions: dict = None,
        models_definition: dict = None
    ):
        def _create(app: Bottle, app_module):
            configs = dict(
                info=dict(
                    title=title,
                    description=description,
                    version=version,
                ),
                basePath=base_path,
                securityDefinitions=security_definitions,
                definitions=models_definition,
                paths=dict(),
            )

            meta = getattr(app_module, Types.META)
            modules = meta['modules']
            controllers = meta['controllers']

        return _create

    @staticmethod
    def __resolve_modules():
        pass
