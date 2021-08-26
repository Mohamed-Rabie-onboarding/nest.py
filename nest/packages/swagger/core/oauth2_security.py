class __Oauth2SecurityFlow:
    implicit = "implicit"
    password = "password"
    application = "application"
    accessCode = "accessCode"


class Oauth2Security:

    def __init__(
        self,
        description: str = None,
        flow: str = None,
        authorization_url: str = None,
        token_url: str = None,
        scopes: dict = None,
        **kwargs
    ):
        self.configs = {
            "type": "oauth2",
            "description": description,
            "flow": flow,
            "authorizationUrl": authorization_url,
            "tokenUrl": token_url,
            "scopes": scopes,
            **kwargs
        }

    flow = __Oauth2SecurityFlow()

    @staticmethod
    def scopes(**kwargs):
        for key, value in kwargs.items():
            print(key, value)
