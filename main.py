from nest import NestFactory
from example.app_module import AppModule
from nest.packages.swagger import SwaggerFactory, Info, Tag, SecurityDefinitions, Oauth2Security, Oauth2SecurityFlow, Definitions, Model, ModelType, ModelFormat


def main():

    swagger = SwaggerFactory(
        swagger='2.0',
        info=Info(
            title='Swagger Petstore',
            description="This is a sample server Petstore server.  You can find out more about     Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).      For this sample, you can use the api key `special-key` to test the authorization     filters.",
            version='1.0.0',
            terms_of_service="http://swagger.io/terms/",
            contact=Info.contact(
                name="Hola",
                url='http://swagger.io/terms/',
                email="apiteam@swagger.io"
            ),
            license=Info.license(
                name="Apache 2.0",
                url="http://www.apache.org/licenses/LICENSE-2.0.html"
            )
        ),
        base_path="/api/v1",
        tags=[
            Tag(
                name='pet',
                description='Everything about your Pets',
                external_docs=Tag.external_docs(
                    description="Find out more",
                    url="http://swagger.io",
                )
            ),
            Tag(
                name='store',
                description='Everything about your Pets',
            ),
            Tag(
                name='user',
                description='Operations about user',
                external_docs=Tag.external_docs(
                    description="Find out more about our store",
                    url="http://swagger.io",
                )
            ),
        ],
        schemes=['http', 'https'],
        security_definitions=SecurityDefinitions(
            petstore_auth=Oauth2Security(
                authorization_url="http://petstore.swagger.io/oauth/dialog",
                flow=Oauth2SecurityFlow.implicit,
                scopes=Oauth2Security.scopes(
                    ("write:pets", "modify pets in your account"),
                    ("read:pets", "read your pets")
                )
            )
        ),
        definitions=Definitions(
            Order=Model(
                model_type=ModelType.object,
                properties=Model.properties(
                    id=Model(
                        model_type=ModelType.integer,
                        format=ModelFormat.int64
                    ),
                    petId=Model(
                        model_type=ModelType.integer,
                        format=ModelFormat.int32
                    ),
                    quantity=Model(
                        model_type=ModelType.integer,
                        format=ModelFormat.int32
                    ),
                    shipDate=Model(
                        model_type=ModelType.string,
                        format=ModelFormat.date_time
                    ),
                    status=Model(
                        model_type=ModelType.string,
                        description='Order Status',
                        enum=['placed', 'approved', 'delivered']
                    ),
                    complete=Model(
                        model_type=ModelType.boolean,
                        default=False
                    )
                ),
                xml=Model.xml(
                    name='Order'
                ),
                required=['id', 'petId', 'quantity',
                          'shipDate', 'status', 'complete']
            )
        )
    )

    app = NestFactory.create(AppModule)

    swagger.setup(app, '/docs')
    app.listen(3000)


if __name__ == "__main__":
    main()
