from nest.scripts import Types
from nest.scripts import assert_list

__assert_list = assert_list('`nest_error` decorator')


def nest_error(injects: list = None):
    """
    Marks a class as an error_handler.

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
    >>> @nest_error(
    >>>     injects=[]
    >>> )
    >>> class AppError:
    >>> 
    >>>     @error(400)
    >>>     def error_400_handler(self, ctx: AppContext):
    >>>         res = ctx.res
    >>>         res.set_header('content-type', 'application/json')
    >>>         error = ctx.error # <instance 'HTTPError'>
    >>> 
    >>>         return {
    >>>             'status': 400,
    >>>             'message': 'Bad Request.'
    >>>         }
    >>> 
    >>>     @error(403)
    >>>     def error_403_handler(self):
    >>>         return dumps({
    >>>             'status': 403,
    >>>             'message': 'Forbidden.'
    >>>         })
    >>> 
    >>>     @error(404)
    >>>     def error_404_handler(self, ctx: AppContext):
    >>>         return dumps({
    >>>             'status': 404,
    >>>             'message': 'Page not found.'
    >>>         })
    >>> 

    See Also
    --------
    injectable : 
        Marks a class as a service [More Info](/core/injectable.html).
    nest_module :
        Marks a class as a module [More Info](/core/nest_module.html).
    controller :
        Marks a class as a controller [More Info](/core/controller.html).

    """
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
