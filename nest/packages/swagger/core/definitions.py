from typing import List, Tuple
from nest.packages.swagger.internals import not_none_assign


class ModelFormat:
    int32 = 'int32'
    int64 = 'int64'
    float = 'float'
    double = 'double'
    string = 'string'
    email = 'email'
    byte = 'byte'
    binary = 'binary'
    boolean = 'boolean'
    date = 'date'
    date_time = 'date-time'
    password = 'password'


class ModelType:
    array = 'array'
    boolean = 'boolean'
    integer = 'integer'
    null = 'null'
    number = 'number'
    object = 'object'
    string = 'string'


class Model:

    def __init__(
        self,
        ref: str = None,
        default: str = None,
        description: str = None,
        discriminator: str = None,
        exclusive_maximum: bool = None,
        exclusive_minimum: bool = None,
        format: str = None,
        maximum: int = None,
        max_items: int = None,
        max_length: int = None,
        max_properties: int = None,
        minimum: int = None,
        min_items: int = None,
        min_length: int = None,
        min_properties: int = None,
        multiple_of: int = None,
        pattern: str = None,
        model_type: str = None,
        title: str = None,
        read_only: bool = None,
        unique_items: bool = None,
        items=None,
        enum: list = None,
        external_docs: dict = None,
        example=None,
        additional_properties=None,
        required: List[str] = None,
        properties=None,
        xml: dict = None,
        all_of: List = None,
        **kwargs
    ):
        configs = {}
        assign_configs = not_none_assign(configs)

        assign_configs(ref, '$ref', f'#/definitions/{ref}')
        assign_configs(default, 'default')
        assign_configs(description, 'description')
        assign_configs(discriminator, 'discriminator')
        assign_configs(exclusive_maximum, 'exclusiveMaximum')
        assign_configs(exclusive_minimum, 'exclusiveMinimum')
        assign_configs(format, 'format')
        assign_configs(maximum, 'maximum')
        assign_configs(max_items, 'maxItems')
        assign_configs(max_length, 'maxLength')
        assign_configs(max_properties, 'maxProperties')
        assign_configs(minimum, 'minimum')
        assign_configs(min_items, 'minItems')
        assign_configs(min_length, 'minLength')
        assign_configs(min_properties, 'minProperties')
        assign_configs(multiple_of, 'multipleOf')
        assign_configs(pattern, 'pattern')
        assign_configs(model_type, 'type')
        assign_configs(title, 'title')
        assign_configs(read_only, 'readOnly')
        assign_configs(unique_items, 'uniqueItems')
        assign_configs(enum, 'enum')
        assign_configs(external_docs, 'externalDocs')
        assign_configs(example, 'example')
        assign_configs(required, 'required')
        assign_configs(properties, 'properties')
        assign_configs(xml, 'xml')
        assign_configs(
            items,
            'items',
            items.configs if isinstance(items, Model) else items
        )
        assign_configs(
            additional_properties,
            'additionalProperties',
            additional_properties.configs if isinstance(
                additional_properties, Model) else additional_properties
        )
        assign_configs(
            all_of,
            'allOf',
            [of.configs if isinstance(of, Model) else of for of in all_of] if type(
                all_of) is list else all_of
        )

        self.configs = {
            **configs,
            **kwargs
        }

    @staticmethod
    def external_docs(description: str = None, url: str = None, **kwargs):
        return {
            'description': description,
            'url': url,
            **kwargs
        }

    @staticmethod
    def properties(**kwargs: Tuple[Tuple]):
        configs = {}
        for key, value in kwargs.items():
            configs[key] = value.configs if isinstance(value, Model) else value
        return configs

    @staticmethod
    def xml(
        attribute: bool = None,
        name: str = None,
        namespace: str = None,
        prefix: str = None,
        wrapped: bool = None,
        **kwargs
    ):
        return {
            'attribute': attribute,
            'name': name,
            'namespace': namespace,
            'prefix': prefix,
            'wrapped': wrapped,
            **kwargs
        }


class Definitions:

    def __init__(self, **kwargs: Tuple[Tuple[str, Model]]):
        configs = {}
        for key, value in kwargs.items():
            configs[key] = value.configs if isinstance(value, Model) else value
        self.configs = configs
