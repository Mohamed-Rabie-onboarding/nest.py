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
        configs = dict(
            info=dict(
                title=title,
                description=description,
                version=version,
            ),
            basePath=base_path,
            securityDefinitions=security_definitions,
            paths=dict(),
            definitions=models_definition
        )

        def _create(app: Bottle, app_module):
            print(configs)

        return _create
