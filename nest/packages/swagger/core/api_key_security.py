class __ApiKeySecurityIn:
    header = 'header'
    query = 'query'


class ApiKeySecurity:

    def __init__(self, key_in: str = None, name: str = None, description: str = None, **kwargs):
        self.configs = {
            'type': 'apiKey',
            'in': key_in,
            'name': name,
            'description': description,
            **kwargs
        }

    key_in = __ApiKeySecurityIn()
