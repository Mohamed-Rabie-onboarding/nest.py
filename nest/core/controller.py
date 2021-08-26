from nest.scripts.types import Types
from nest.scripts.assert_type import assert_str, assert_list

__assert_str = assert_str('`controller` decorator')
__assert_list = assert_list('`controller` decorator')


def controller(prefix: str = None, injects: list = None):
    """
    Marks a class as a controller.

    Adding a meta attribute with controller configs which allows to
    initialize class correctly with the required options also accepts
    a prefix which will be used later with routes.

    Parameters
    ----------
    prefix : str
        A string that will be appended before each route's uri.
    injects : list
        A list of required services that should be passed into the
        controller should it can perform correctly.

    Returns
    -------
    function(Ctor) -> Ctor
        Returns a function that takes a class and returns it after registering meta on it.

    Examples
    --------
    >>> @controller({
    >>>     prefix='/user',
    >>>     injects=[
    >>>         UserService
    >>>     ]
    >>> })
    >>> class UserController:
    >>> 
    >>>     def __init__(self, userService: UserService):
    >>>         self.userService = userService

    See Also
    --------
    nest_error :  
        Marks a class as an error_handler [More Info](/core/nest_error.html).
    nest_module :
        Marks a class as a module  [More Info](/core/nest_module.html).
    injectable :
        Marks a class as a service  [More Info](/core/injectable.html).

    """
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
