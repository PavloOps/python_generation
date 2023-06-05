from datetime import date
from urllib.parse import urlencode


def power(x):
    return lambda num: num**x


def generator_square_polynom(a, b, c):
    return lambda x: a*x**2 + b*x + c


def sourcetemplate(url):
    def combine(**kwargs):
        if kwargs:
            sorted_values = sorted(kwargs.items(), key=lambda val: val[0])
            return f"{url}?{urlencode(sorted_values)}"
        else:
            return url
    return combine


def date_formatter(country_code):
    def format_date(input_date):
        d = {'ru': '%d.%m.%Y',
             'us': '%m-%d-%Y',
             'ca': '%Y-%m-%d',
             'br': '%d/%m/%Y',
             'fr': '%d.%m.%Y',
             'pt': '%d-%m-%Y', }
        return input_date.strftime(d[country_code])
    return format_date
