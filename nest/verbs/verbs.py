from nest.scripts.types import Types
from .create_route import create_route

get = create_route(Types.GET)
post = create_route(Types.POST)
put = create_route(Types.PUT)
patch = create_route(Types.PATCH)
delete = create_route(Types.DELETE)
