from nest.scripts import Types
from nest.scripts import assert_list

__assert_list = assert_list('`nest_error` decorator')


def nest_error(injects: list = None):
    __assert_list(injects, 'injects')

    def _nest_error(Ctor):
        setattr(
            Ctor,
            Types.META,
            dict(
                type=Types.ERROR,
                injects=injects if type(injects) is list else []
            )
        )

        return Ctor

    return _nest_error
