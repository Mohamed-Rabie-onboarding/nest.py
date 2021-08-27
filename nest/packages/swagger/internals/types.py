class Types:

    def prefix(p: str):
        return f'@@__SWAGGER_{p}__@@'

    SUMMARY =           prefix('SUMMARY')
    TAGS =              prefix('TAGS')
    SCHEMES =           prefix('SCHEMES')
    OPERATION_ID =      prefix('OPERATION_ID')
    CONSUMES =          prefix('CONSUMES')
    DEPRECATED =        prefix('DEPRECATED')
    DESCRIPTION =       prefix('DESCRIPTION')
    PRODUCES =          prefix('PRODUCES')
    SECURITY =          prefix('SECURITY')
    EXTERNAL_DOCS =     prefix('EXTERNAL_DOCS')
    PARAMETERS =        prefix('PARAMETERS')
    RESPONSES =         prefix('RESPONSES')


__TYPE_TO_KEY__ = dict()
__TYPE_TO_KEY__[Types.SUMMARY] = 'summary'
__TYPE_TO_KEY__[Types.TAGS] = 'tags'
__TYPE_TO_KEY__[Types.SCHEMES] = 'schemes'
__TYPE_TO_KEY__[Types.OPERATION_ID] = 'operationId'
__TYPE_TO_KEY__[Types.CONSUMES] = 'consumes'
__TYPE_TO_KEY__[Types.DEPRECATED] = 'deprecated'
__TYPE_TO_KEY__[Types.DESCRIPTION] = 'description'
__TYPE_TO_KEY__[Types.PRODUCES] = 'produces'
__TYPE_TO_KEY__[Types.SECURITY] = 'security'
__TYPE_TO_KEY__[Types.EXTERNAL_DOCS] = 'externalDocs'
__TYPE_TO_KEY__[Types.PARAMETERS] = 'parameters'
__TYPE_TO_KEY__[Types.RESPONSES] = 'responses'


def type_to_key(t):
    return __TYPE_TO_KEY__[t]