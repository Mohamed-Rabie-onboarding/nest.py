
from typing import List, Tuple
from nest.packages.swagger.internals import Types


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


def api_response(
    status: int = None,
    description: str = None,
    schema: dict = None,
    headers: dict = None,
    examples: dict = None
):
    def _api_response(Ctor):
        return Ctor
    return _api_response


def api_parameter():
    def _api_parameter(Ctor):
        return Ctor
    return _api_parameter
