# task 2
convert = lambda num: tuple(n.upper().replace(f"0{char}", "") \
                            for n, char in zip((bin(num), oct(num), hex(num)), tuple("BOX")))

# task 3
from statistics import mean
films = {'Spider-Man: No Way Home': {'imdb': 8.8, 'kinopoisk': 8.3},
         'Don"t Look Up': {'imdb': 7.3, 'kinopoisk': 7.6},
         'Encanto': {'imdb': 7.3, 'kinopoisk': 7.4},
         'The Witcher': {'imdb': 8.2, 'kinopoisk': 7.3},
         'Ghostbusters: Afterlife': {'imdb': 7.3, 'kinopoisk': 8},
         'Harry Potter 20th Anniversary: Return to Hogwarts': {'imdb': 8.1, 'kinopoisk': 8.2},
         'Shingeki no Kyojin': {'imdb': 9.0, 'kinopoisk': 8.3},
         'The Matrix': {'imdb': 8.7, 'kinopoisk': 8.5},
         'The Dark Knight': {'imdb': 9.0, 'kinopoisk': 8.5},
         'The Shawshank Redemption': {'imdb': 9.3, 'kinopoisk': 9.1},
         'Avengers: Endgame': {'imdb': 8.4, 'kinopoisk': 7.7}}

print(min(films, key=lambda x: mean(films[x].values())))

# task 4
non_negative_even = lambda x: all(num > -1 and not num%2 for num in x)

# task 6
def is_greater(lists, num):
    return sum(max(lists, key=sum)) > num

# task 7
def custom_isinstance(objects, typeinfo):
    return sum(isinstance(obj, typeinfo) for obj in objects)

# task 8
numbers = [-7724, 5023, 3197, -102, -4129, -880, 5857, -2866, -8913, 1195, 9809, 5347, -8071, 903, 3030,
           -4347, -3354, 1024, 8670, 4210, -5228, 8900, 4823, -2002, 4900, 9520, -3658, 1104, -9554, 3064,
           9632, -8701, 3384, 4370, 2034, 7822, -9694, 3347, 7440, -8459, 3238, -5193, -3381, 5281, 9022, 5559,
           7593, -6540, -6204, -2483, 8729, 5810, -8254, -9846, -1801, 4882, 3838, -3140, 7609, -3325, 6026, 2994,
           -1677, 1266, -1893, -4408, -5722, -2841, 9812, 5837, -7474, 4624, -664, 6998, 7888, -971, 8810, 3812, -5396,
           2593, 512, -4634, 9735, -3062, 9031, -9300, 3657, 6332, 7552, 8125, -725, 4392, 1727, 8194, -2828, -4314,
           -8967, -7912, -1363, -5957]
print(max(enumerate(numbers), key=lambda x: x[1])[0])

# task 9
my_pow = lambda num: sum(x**pow for pow, x in enumerate(map(int, str(num)), 1))

# task 10
names = ['Moana', 'Cars', 'Zootopia', 'Ratatouille', 'Coco', 'Inside Out', 'Finding Nemo', 'Frozen']
budgets = [150000000, 120000000, 150000000, 150000000, 180000000, 175000000, 94000000, 150000000]
box_offices = [643331111, 462216280, 1023784195, 620702951, 807082196, 857611174, 940335536, 1280802282]


total_box = dict(zip(names, [y-x for x, y in zip(budgets, box_offices)]))
[print(f"{key}: {value}$") for key, value in sorted(total_box.items())]


# task 11
def zip_longest(*args, fill=None):
    size = len(max(args, key=len))
    data = [item+[fill]*(size-len(item)) for item in args]
    return list(zip(*data))

# task 12
pattern = [*range(97, 123), *range(65,91), *range(49, 58, 2), *range(48, 58, 2)]
print("".join(sorted(input(), key=lambda x: pattern.index(ord(x)))))

### PART 2 ###

# task 1
def hash_as_key(obj):
    result = dict()
    for item in obj:
        key = hash(item)
        if key in result:
            if isinstance(result[key], list):
                result[key].extend([item])
            else:
                result[key] = [result[key], item]
        else:
            result[key] = item
    return result


# task 2
operations = {
    list: lambda x: x[-1],
    tuple: lambda x: x[0],
    set: lambda x: len(x),
}

it = eval(input())
print(operations[type(it)](it))

# task 3
print(max(eval(x) for x in open(0)))

# task 4
func = input()
a, b = map(int, input().split())
values = [eval(func) for x in range(a, b+1)]

print(f'''Минимальное значение функции {func} на отрезке [{a}; {b}] равно {min(values)}
Максимальное значение функции {func} на отрезке [{a}; {b}] равно {max(values)}''')


### PART 3 ###

# task 1
data = ['Timur', -16.648911695768902, 'six', -202, 883.0093275936454, -765, (3, 4),
        -105.10718000213546, 976, -308.96857946288094, 458, ['one', 'two'], 479.92207220345927, -87, -71,
        'twelve', 112, -621, -715.0179551194733, 'seven', 229, 729, -358, [1, 2, 3], -974, 882, -894.4709033242768,
        '', 323.7720806756133, 'beegeek', -224, 431, 170.6353248658936, -343.0016746052049, 'number',
        104.17133679352878, [], -353.5964777099863, 'zero',
        -113, 288, None, -708.3036176571618]

print(*map(int, (x for x in data if isinstance(x, (float, int)))), sep="\n")

# task 2
numbers = [4754, -4895, -364, -4764, 4683, 1639, -43, 228, -2701, -1503, 1223, 4340,
           -1296, 3939, -345, 623, -3275, 1003, 4367, -1739, 550, -1217, -1334, 1526,
           -4359, -3028, -4663, 3356, 3887, 4297, -1982, 1013, 3299, 3556, -3324, 417,
           3531, -3134, 1782, 4439, 1652, -985, 4327, 1517, 1225, -915, 2808, -3851,
           -1005, 3396, 2842, -3879, -3824, -3805, 1609, -4741, -3072, 3573, 4680,
           588, -1430, 2378, -1095, -343, 4357, -2164, -3304, 4354, 4926, -352,
           -1187, -3313, 2741, 4786, -2689, 741, 4558, 1442, 62, -1099, -2201,
           -16, -3115, 1862, 2384, 4072, -90, 204, 1158, -3134, -2512, 756,
           4148, 4370, 1756, 3609, -1148, -3909, 4123, -2906, 69, 96, 1111]

print(sum(x**2 for x in numbers if not x%9 and x in range(-100, 101)))

# task 3
names = ['ульяна', 'арина', 'Дмитрий', 'Сергей', 'Яна', 'мила', 'Ольга', 'софья', 'семён', 'Никита',
         'маргарита', 'Василиса', 'Кирилл', 'александр', 'александра', 'Иван', 'андрей', 'Родион',
         'максим', 'алиса', 'Артём', 'софия', 'владимир', 'дамир', 'Валерий', 'степан', 'Алексей', 'Марк',
         'олег', 'ирина', 'Милана', 'мия', 'денис', 'Фёдор', 'Елизавета', 'айлин', 'Варвара', 'валерия',
         'Алёна', 'Николь', 'юлия', 'Ксения', 'пётр', 'георгий', 'Мария', 'глеб', 'илья', 'Захар', 'Дарья',
         'Евгения', 'матвей', 'Серафим', 'екатерина', 'Тимофей', 'виктор', 'Егор', 'Ника', 'анна', 'даниил',
         'тихон', 'вера', 'кира', 'Эмилия', 'Виктория', 'Игорь', 'полина', 'алина', 'Давид', 'анастасия',
         'Вероника', 'ярослав', 'Руслан', 'татьяна', 'Демид', 'амелия', 'Элина', 'Арсен', 'евгений',
         'мадина', 'дарина', 'Савелий', 'Платон', 'Аделина', 'диана', 'Айша', 'павел', 'Стефания',
         'Тимур', 'Ева', 'Елисей', 'Артемий', 'григорий', 'Мирон', 'Мирослава', 'Мира', 'Марат',
         'Лилия', 'роман', 'владислав', 'Леонид']


print(*sorted(x.title() for x in names if x[0].lower() in "ам" and len(x)>3), sep=" ")

# task 4
d = {1: 1, 2: 1}
fib = lambda x: d[x] if x in d else d.setdefault(x, fib(x - 1) + fib(x - 2))

# task 5
def print_operation_table(operation=None, rows=None, cols=None):
    [print(*[operation(n, m) for m in range(1, cols+1)]) for n in range(1, rows+1)]

# task 6
from string import ascii_letters, ascii_uppercase, ascii_lowercase, digits

def verification(login, password, success, failure):
    check_pass = set(password)
    check_set = {
        ascii_letters: "в пароле нет ни одной буквы",
        ascii_uppercase: "в пароле нет ни одной заглавной буквы",
        ascii_lowercase: "в пароле нет ни одной строчной буквы",
        digits: "в пароле нет ни одной цифры"
    }

    for pattern, message in check_set.items():
        if check_pass.isdisjoint(pattern):
            return failure(login, message)
    else:
        return success(login)

def success(login):
    print(f'Привет, {login}!')

def failure(login, text):
    print(f'{login}, попробуйте снова. Ошибка: {text}')

# verification('timyrik20', 'Beegeek314', success, failure)

# task 7
def remove_marks(text, marks):
    for symbol in marks:
        text = text.replace(symbol, '')
    else:
        remove_marks.count += 1
        return text
remove_marks.count = 0

marks = '.,!?'
text = 'Are you listening? Meet my family! There are my parents, my brother and me.'

for mark in marks:
    print(remove_marks(text, mark))

print(remove_marks.count)