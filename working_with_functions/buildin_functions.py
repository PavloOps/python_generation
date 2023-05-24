# task 2
convert = lambda num: tuple(n.upper().replace(f"0{char}", "") \
                            for n, char in zip((bin(num), oct(num), hex(num)), tuple("BOX")))

# task 3
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
