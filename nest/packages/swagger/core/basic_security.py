class BasicSecurity:

    def __init__(self, description: str = None, **kwargs):
        self.configs = {
            'type': 'basic',
            'description': description,
            **kwargs
        }
