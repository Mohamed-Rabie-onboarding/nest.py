from nest.scripts.types import Types
from .create_route import create_route

Get = create_route(Types.GET)
Post = create_route(Types.POST)
Put = create_route(Types.PUT)
Patch = create_route(Types.PATCH)
Delete = create_route(Types.DELETE)
