class Types:
    def prefix(name: str):
        return f'@@__NEST_{name}__@@'

    meta =          prefix('META')
    controller =    prefix('CONTROLLER')
    injectable =    prefix('INJECTABLE')
    module =        prefix('MODULE')
    get =           prefix('GET')
    post =          prefix('POST')
    PUT =           prefix('PUT')
    PATCH =         prefix('PATCH')
    DELETE =        prefix('DELETE')