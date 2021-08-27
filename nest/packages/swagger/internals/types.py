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
    PARAMETER =         prefix('PARAMETER')
    RESPONSE =          prefix('RESPONSE')
