class SecurityDefinitions:

    def __init__(self, **kwargs):
        configs = {}
        for key, value in kwargs.item():
            configs[key] = value.configs
        self.configs = configs
