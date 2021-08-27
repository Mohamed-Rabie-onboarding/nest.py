
from nest.packages.swagger.core.definitions import Model, ModelType
from typing import List, Tuple, Union
from nest.packages.swagger.internals import Types, not_none_assign


def __api_basic_prop(t: str):
    def api_basic_prop(value):
        def _api_basic_prop(Ctor):
            setattr(Ctor, t, value)
            return Ctor
        return _api_basic_prop
    return api_basic_prop


api_summary = __api_basic_prop(Types.SUMMARY)
api_description = __api_basic_prop(Types.DESCRIPTION)
api_deprecated = __api_basic_prop(Types.DEPRECATED)
api_operation_id = __api_basic_prop(Types.OPERATION_ID)
api_tags = __api_basic_prop(Types.TAGS)
api_schemes = __api_basic_prop(Types.SCHEMES)
api_produces = __api_basic_prop(Types.PRODUCES)
api_consumes = __api_basic_prop(Types.CONSUMES)


def api_external_docs(description: str = None, url: str = None):
    def _api_external_docs(Ctor):
        setattr(
            Ctor,
            Types.EXTERNAL_DOCS,
            {
                'description': description,
                'url': url
            }
        )
        return Ctor
    return _api_external_docs


def api_security(**kwargs: Tuple[Tuple[str, List[str]]]):
    def _api_security(Ctor):
        configs = {}
        for key, value in kwargs.items():
            configs[key] = value
        setattr(
            Ctor,
            Types.SECURITY,
            configs
        )
        return Ctor
    return _api_security


""" 
TODO: define response & parameter
"""


def __resolve_schema(schema):
    if schema is None:
        return None
    if isinstance(schema, Model):
        return schema.configs
    if type(schema) is str:
        if schema.endswith('[]'):
            return {
                'type': ModelType.array,
                'items': {
                    '$ref': f'#/definitions/{schema[:-2]}'
                }
            }
        return {
            '$ref': f'#/definitions/{schema}'
        }
    raise TypeError('Schema must be of type Model or str')


def api_response(
    status: int = None,
    description: str = None,
    schema: Union[Model, str] = None,
    headers: dict = None,
    examples: dict = None,
):
    def _api_response(Ctor):
        if type(status) is not int:
            raise TypeError('http_status must be provided!')
        configs = {}
        assign_configs = not_none_assign(configs)

        assign_configs(description, 'description')
        assign_configs(headers, 'headers')
        assign_configs(examples, 'examples')
        assign_configs(__resolve_schema(schema), 'schema')

        if not hasattr(Ctor, Types.RESPONSES):
            setattr(Ctor, Types.RESPONSES, {})

        res = getattr(Ctor, Types.RESPONSES)
        res[status] = configs

        return Ctor
    return _api_response


def api_parameter(
    name: str = None,
    param_in: str = None,
    description: str = None,
    required: bool = None,
    schema: Union[Model, str] = None
):
    def _api_parameter(Ctor):
        configs = {}
        assign_configs = not_none_assign(configs)

        assign_configs(description, 'description')
        assign_configs(name, 'name')
        assign_configs(param_in, 'in')
        assign_configs(required, 'required')
        assign_configs(__resolve_schema(schema), 'schema')

        if not hasattr(Ctor, Types.PARAMETERS):
            setattr(
                Ctor,
                Types.PARAMETERS,
                []
            )

        params: list = getattr(Ctor, Types.PARAMETERS)
        params.append(configs)

        return Ctor
    return _api_parameter
