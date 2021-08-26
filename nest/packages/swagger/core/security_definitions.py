class SecurityDefinitions:

    def __init__(self, **kwargs):
        configs = {}
        for key, value in kwargs.items():
            configs[key] = value.configs
        self.configs = configs
