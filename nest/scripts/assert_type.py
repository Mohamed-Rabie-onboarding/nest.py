def assert_type(excepted_type, type_name):
    def _assert_type(in_name: str):
        def __assert_type(value, param_name: str):
            if value is not None and type(value) is not excepted_type:
                raise TypeError(
                    f'Excepted `{param_name}` of type [{type_name}] but found {type(value)} in {in_name}.',
                )
        return __assert_type
    return _assert_type


assert_str = assert_type(str, 'str')
assert_list = assert_type(list, 'list')
