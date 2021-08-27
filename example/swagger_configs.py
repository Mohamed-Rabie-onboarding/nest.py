from nest.packages.swagger import SwaggerFactory, Info, Definitions, Model, ModelType

cat_model = Model(
    model_type=ModelType.object,
    properties=Model.properties(
        id=Model(
            model_type=ModelType.integer,
            example=1,
            description='Cat ID',
        ),
        name=Model(
            model_type=ModelType.string,
            example='cat 0',
            description='Cat name'
        )
    ),
    required=['id', 'name']
)

cat_input = Model(
    model_type=ModelType.object,
    properties=Model.properties(
        name=Model(
            model_type=ModelType.string,
            example='cat 0',
            description='Cat name'
        )
    ),
    required=['name']
)

swagger_configs = SwaggerFactory(
    swagger='2.0.0',
    base_path='/api/v1',
    info=Info(
        title='Nest Cats Example',
        description='This is an example for how to use nest-swagger package',
        version='v0.1.0'
    ),
    definitions=Definitions(
        Cat=cat_model,
        CatInput=cat_input
    )
)
