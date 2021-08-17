from nest.scripts import Types
from typing import Union


def Controller(config: Union[str, dict] = None):
    def _controller(Ctor):
        prefix = ''
        injects = []

        if config is str:
            prefix = config
        elif config is dict:
            prefix = config.uri if config.uri is not None else prefix
            injects = config.injects if config.injects is not None else injects

        class NEST_Controller(Ctor):
            pass

        setattr(
            NEST_Controller,
            Types.meta,
            dict(
                type=Types.controller,
                prefix=prefix,
                controller=Ctor,
                injects=injects,
                routes=[]
            )
        )

        return NEST_Controller
    return _controller
