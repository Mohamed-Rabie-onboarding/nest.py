from nest import NestFactory
from example.app_module import AppModule
# from nest.packages.swagger import SwaggerFactory, security_definition, define_model


def main():
    app = NestFactory.create(AppModule)

    # swagger = SwaggerFactory.create(
    #     title='example',
    #     base_path='/api/v1',
    #     description='Example',
    #     version='v1.0.0',
    #     security_definitions=dict(
    #         ApiKeyAuth=security_definition(
    #             type="apiKey",
    #             found_in="header",
    #             name="Authorization",
    #             description="Token u got from login user /user/authenticate"
    #         )
    #     ),
    #     models_definition=dict(
    #         User=define_model(
    #             type="object",
    #             properties=dict(
    #                 id=dict(
    #                     type="integer",
    #                     example=1
    #                 )
    #             )
    #         )
    #     )
    # )
    # app.use(swagger)

    app.listen(3000)


if __name__ == "__main__":
    main()
