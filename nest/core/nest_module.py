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
