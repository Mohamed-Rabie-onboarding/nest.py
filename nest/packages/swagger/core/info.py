class Info:

    def __init__(
        self,
        title: str = None,
        version: str = None,
        description: str = None,
        terms_of_service: str = None,
        contact: dict = None,
        license: dict = None,
        **kwargs
    ):
        self.configs = {
            'title': title,
            'version': version,
            'description': description,
            'termsOfService': terms_of_service,
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
