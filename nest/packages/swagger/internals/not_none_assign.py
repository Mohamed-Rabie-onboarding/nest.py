def not_none_assign(object):
    def _not_none_assign(value, key, new_value=None):
        if value is not None:
            object[key] = new_value or value
    return _not_none_assign
