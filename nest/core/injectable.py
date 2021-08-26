from nest.scripts.types import Types
from nest.scripts.assert_type import assert_list

__assert_list = assert_list('`injectable` decorator')


def injectable(injects: list = None):
    """
    Marks a class as a service.

    Adding a meta attribute with service configs which allows to
    initialize class correctly with the required options.

    Parameters
    ----------
    injects : list
        A list of required services that should be passed into the
        controller should it can perform correctly.

    Returns
    -------
    function(Ctor) -> Ctor
        Returns a function that takes a class and returns it after registering meta on it.

    Examples
    --------
    >>> @injectable(
    >>>     injects=[]
    >>> )
    >>> class UserService:
    >>>     users = []
    >>> 
    >>>     def get_users(self):
    >>>         return self.users

    See Also
    --------
    nest_error : 
        Marks a class as an error_handler [More Info](/core/nest_error.html).
    nest_module :
        Marks a class as a module [More Info](/core/nest_module.html).
    controller :
        Marks a class as a controller [More Info](/core/controller.html).

    """
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
