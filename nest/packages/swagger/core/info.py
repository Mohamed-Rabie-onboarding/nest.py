class Info:

    def __init__(
        self,
        title: str = None,
        version: str = None,
        description: str = None,
        termsOfService: str = None,
        contact: dict = None,
        license: dict = None,
        **kwargs
    ):
        self.configs = {
            'title': title,
            'version': version,
            'description': description,
            'termsOfService': termsOfService,
            'contact': contact,
            'license': license,
            **kwargs
        }

    @staticmethod
    def contact(name: str = None, url: str = None, email: str = None, **kwargs):
        return {
            'name': name,
            'url': url,
            'email': email,
            **kwargs
        }

    @staticmethod
    def license(name: str = None, url: str = None, **kwargs):
        return {
            'name': name,
            'url': url,
            **kwargs
        }
