class Types:
    def prefix(name: str):
        return f'@@__NEST_{name}__@@'

    META =          prefix('META')
    CONTROLLER =    prefix('CONTROLLER')
    INJECTABLE =    prefix('INJECTABLE')
    MODULE =        prefix('MODULE')
    GET =           prefix('GET')
    POST =          prefix('POST')
    PUT =           prefix('PUT')
    PATCH =         prefix('PATCH')
    DELETE =        prefix('DELETE')
    ERROR =         prefix('ERROR')


__TYPE_TO_VERB__ = dict()
__TYPE_TO_VERB__[Types.GET]     = 'GET'
__TYPE_TO_VERB__[Types.POST]    = 'POST'
__TYPE_TO_VERB__[Types.PUT]     = 'PUT'
__TYPE_TO_VERB__[Types.PATCH]   = 'PATCH'
__TYPE_TO_VERB__[Types.DELETE]  = 'DELETE'


def type_to_verb(type):
    return __TYPE_TO_VERB__[type]