def power(x):
    return lambda num: num**x


def generator_square_polynom(a, b, c):
    return lambda x: a*x**2 + b*x + c


from urllib.parse import urlencode


def sourcetemplate(url):
    def combine(**kwargs):
        if kwargs:
            sorted_values = sorted(kwargs.items(), key=lambda val: val[0])
            return f"{url}?{urlencode(sorted_values)}"
        else:
            return url
    return combine
