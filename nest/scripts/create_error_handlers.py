from typing import Union
from .create_error_callback import create_error_callback
from .app_context import AppContext


def create_error_handlers(errors: Union[dict, None], ctx: AppContext):
    if errors is None:
        return None

    error_handler = {}
    for status, callback in errors.items():
        error_handler[status] = create_error_callback(callback, ctx)

    return error_handler
