from nest.scripts.types import Types

__TYPE_TO_VERB__ = dict()
__TYPE_TO_VERB__[Types.GET] = 'GET'
__TYPE_TO_VERB__[Types.POST] = 'POST'
__TYPE_TO_VERB__[Types.PUT] = 'PUT'
__TYPE_TO_VERB__[Types.PATCH] = 'PATCH'
__TYPE_TO_VERB__[Types.DELETE] = 'DELETE'


def type_to_verb(type):
    return __TYPE_TO_VERB__[type]
