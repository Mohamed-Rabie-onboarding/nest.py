from typing import Tuple


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

    @staticmethod
    def scopes(*args: Tuple[Tuple[str, str]]):
        configs = {}
        for key, value in args:
            configs[key] = value
        return configs


class Oauth2SecurityFlow:
    implicit = "implicit"
    password = "password"
    application = "application"
    accessCode = "accessCode"
