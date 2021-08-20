from nest.scripts import Types
from nest.scripts import assert_list

__assert_list = assert_list('`injectable` decorator')


def injectable(injects: list = None):
    __assert_list(injects, 'injects')

    def _injectable(Ctor):
        setattr(
            Ctor,
            Types.META,
            dict(
                type=Types.INJECTABLE,
                injects=injects or []
            )
        )

        return Ctor
    return _injectable
