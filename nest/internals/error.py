from nest.scripts.types import Types


class NestError:
    @staticmethod
    def compile(Err, services: dict):
        if Err is None:
            return None
        injects = NestError.get_meta(Err)
        error = Err(*[services[i] for i in injects])
        error_handler = {}
        for key in error.__dir__():
            route = getattr(error, key)
            if key.startswith('__') or not callable(route) or not hasattr(route, Types.META):
                continue
            http_status = NestError.get_route_meta(route)
            error_handler[http_status] = route
        return {
            'error': error,
            'error_handler': error_handler
        }

    @staticmethod
    def get_meta(err):
        meta = getattr(err, Types.META)
        assert meta['type'] == Types.ERROR
        return meta['injects']

    @staticmethod
    def get_route_meta(route):
        meta = getattr(route, Types.META)
        assert meta['type'] == Types.ERROR
        return meta['status']
