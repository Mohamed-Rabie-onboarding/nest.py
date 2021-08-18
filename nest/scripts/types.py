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