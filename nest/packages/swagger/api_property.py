from typing import List, Union
from .swagger_types import SwaggerTypes


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
            SwaggerTypes.ROUTE,
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


def api_response(http_status: int, description: str = None, schema: Union[dict, str] = None):
    def _api_response(Ctor):
        status = str(http_status)

        if not hasattr(Ctor, SwaggerTypes.RESPONSE):
            setattr(
                Ctor,
                SwaggerTypes.RESPONSE,
                {}
            )

        responses = getattr(Ctor, SwaggerTypes.RESPONSE)

        if hasattr(responses, status):
            raise Exception(f'Cannot assign `{status}` http_status twice.')

        responses[status] = dict(
            description=description or '',
            schema=response_schema(schema)
        )

        return Ctor
    return _api_response
