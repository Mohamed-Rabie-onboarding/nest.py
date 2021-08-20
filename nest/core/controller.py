from nest.scripts import Types
from nest.scripts import assert_str, assert_list

__assert_str = assert_str('`controller` decorator')
__assert_list = assert_list('`controller` decorator')


def controller(prefix: str = None, injects: list = None):
    __assert_str(prefix, 'prefix')
    __assert_list(injects, 'injects')

    def _controller(Ctor):
        setattr(
            Ctor,
            Types.META,
            dict(
                type=Types.CONTROLLER,
                prefix=prefix or '',
                injects=injects or [],
            )
        )

        return Ctor
    return _controller
