from typing import List, Union


def api_property(tags: List[str] = None, summary: str = None, description: str = None, responses=dict):
    configs = dict(
        tags=tags,
        summary=summary,
        description=description,
        responses=responses
    )

    def _api_property(Ctor):
        setattr(
            Ctor,
            '@@__SWAGGER__@@',
            configs
        )

        return Ctor
    return _api_property


def response_schema(schema: Union[dict, str]):
    if schema is None:
        return None

    if type(schema) is dict:
        return schema
    return {
        "$ref": f"#/definitions/{schema}"
    }


def api_response(description: str = None, schema: Union[dict, str] = None):
    return dict(
        description=description,
        schema=response_schema(schema)
    )
