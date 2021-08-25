from nest.scripts.types import Types


class Provider:
    @staticmethod
    def compile(Service, services: dict) -> None:
        if services.get(Service) is not None:
            return None
        injects = Provider.get_meta(Service)
        service = Service(*[compile(i, services) for i in injects])
        services[Service] = service
        return None

    @staticmethod
    def get_meta(provider):
        meta = getattr(provider, Types.META)
        assert meta['type'] == Types.INJECTABLE
        return meta['injects']
