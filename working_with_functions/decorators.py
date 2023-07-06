from functools import wraps


def sandwich(func):
    def wrapper(*args, **kwargs):
        print("---- Верхний ломтик хлеба ----")
        res = func(*args, **kwargs)
        print("---- Нижний ломтик хлеба ----")
        return res
    return wrapper


def new_print(func):
    def wrapper(*args, **kwargs):
        args = (x.upper() if isinstance(x, str) else x for x in args)
        kwargs = {k: v.upper() if isinstance(v, str) else v for k, v in kwargs.items()}
        func(*args, **kwargs)
    return wrapper

# print = new_print(print)

def do_twice(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        res = func(*args, **kwargs)
        return res
    return wrapper


def square(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res**2
    return wrapper


def returns_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if isinstance(res, str):
            return res
        else:
            raise TypeError
    return wrapper


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print((f'TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}\nTRACE: возвращаемое значение {func.__name__}(): {repr(res)}'))
        return res
    return wrapper


def prefix(string, to_the_end=False):
    def add_string(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if to_the_end:
                return res + string
            else:
                return string + res
        return wrapper
    return add_string


def takes(*check_list_args):
    def check_types(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res_check = all(
                [isinstance(elem, tuple(check_list_args))
                 for elem in [*args, *kwargs.values()]]
            )

            if not res_check:
                raise TypeError

            return func(*args, **kwargs)
        return wrapper
    return check_types


def add_attrs(**attrs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        wrapper.__dict__ |= attrs
        return wrapper
    return decorator


def ignore_exception(*allowed_exeptions):
    def check_exceptions(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except allowed_exeptions as error:
                print(f"Исключение {error.__class__.__name__} обработано")
        return wrapper
    return check_exceptions


class MaxRetriesException(Exception):
    pass


def retry(times):
    def run_function(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    continue
            else:
                raise MaxRetriesException
        return wrapper
    return run_function