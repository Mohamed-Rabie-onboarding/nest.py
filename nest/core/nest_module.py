from nest.scripts import Types
from nest.scripts import assert_str, assert_list

__assert_str = assert_str('`nest_module` decorator')
__assert_list = assert_list('`nest_module` decorator')


def nest_module(
    prefix: str = None,
    modules: list = None,
    providers: list = None,
    controllers: list = None,
    ctx=None,
    error_handler=None,
    plugins: list = None
):
    """
    Marks a class as a module.

    Adding a meta attribute with that required to create a `Bottle` app
    and config it correctly.

    Parameters
    ----------
    prefix : str
        A global prefix that added into its `sub modules`.
    modules : list
        The sub modules of that `nest_module` which inherit its prefix, 
        providers, plugins, error_handler and ctx.
    providers : list
        The injectable service that will be used to initialize 
        controllers correctly.
    ctx : Any
        Any data including str, dict, class, object, etc...
        passed around the application in every single `route` or `error` call.
        Can be override by passing a new context in a `sub module`.
    error_handler : Any
        A class that have to be marked with `@nest_error()`; used as an error handler
        for the entire app.
        Can be override by passing new `error_handler` in any of `sub modules`
    plugins : list
        A plugin is just a `function(configs) -> function(Ctor) -> Ctor`; A function that
        takes in some configs and returns back a function which gets a Ctor and registering
        some meta or patching Ctor and returning it back.

    Returns
    -------
    function(Ctor) -> Ctor
        Returns a function that takes a class and returns it after registering meta on it.

    Examples
    --------
    >>> @nest_module(
    >>>     prefix='/api/v1',
    >>>     modules=[
    >>>         CatsModule,
    >>>         UserModule
    >>>     ],
    >>>     ctx=dict(
    >>>         hello=lambda: print('hello world from ctx')
    >>>     ),
    >>>     error_handler=AppError,
    >>>     plugins=[
    >>>         # The most simple plugin just returing the cb.
    >>>         lambda cb: lambda *args, **kwargs: cb(*args, **kwargs)
    >>>     ]
    >>> )
    >>> class AppModule:
    >>>     pass
    >>> 

    See Also
    --------
    injectable : 
        Marks a class as a service [More Info](/core/injectable.html).
    nest_error : 
        Marks a class as an error_handler [More Info](/core/nest_error.html).
    controller :
        Marks a class as a controller [More Info](/core/controller.html).

    """
    __assert_str(prefix, 'prefix')
    __assert_list(modules, 'modules')
    __assert_list(providers, 'providers')
    __assert_list(controllers, 'controllers')
    __assert_list(plugins, 'plugins')

    def _nestModule(Ctor):
        setattr(
            Ctor,
            Types.META,
            dict(
                type=Types.MODULE,
                prefix=prefix or '',
                modules=modules or [],
                providers=providers or [],
                controllers=controllers or [],
                ctx=ctx,
                error=error_handler,
                plugins=plugins
            )
        )

        return Ctor

    return _nestModule
