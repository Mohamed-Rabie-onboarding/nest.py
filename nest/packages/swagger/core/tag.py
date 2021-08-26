class Tag:

    def __init__(self, name: str = None, description: str = None, external_docs: dict = None, **kwargs):
        self.configs = {
            'name': name,
            'description': description,
            'externalDocs': external_docs,
            **kwargs
        }

    @staticmethod
    def external_docs(description: str = None, url: str = None, **kwargs):
        return {
            'description': description,
            'url': url,
            **kwargs
        }
