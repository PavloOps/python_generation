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
