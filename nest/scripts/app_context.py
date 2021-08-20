from typing import TypeVar, Generic
from bottle import HTTPError, Request, Response

T = TypeVar('T')


class AppContext(Generic[T]):

    def __init__(
        self,
        req: Request = None,
        res: Response = None,
        params: dict = None,
        query: dict = None,
        error: HTTPError = None,
        ctx: T = None,
    ):
        self.req = req
        self.res = res
        self.params = params
        self.query = query
        self.error = error
        self.ctx = ctx
