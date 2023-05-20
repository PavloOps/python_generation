# from lecture: print(print_numbers(0, 10))


def print_numbers(start, end):
    def rec(num):
        if num <= end:
            print(num)
            rec(num + 1)
    rec(start)


# task 1
def traffic(n):
    if n > 0:
        print('Не парковаться')
        traffic(n - 1)


# task 2
def print_hundred(start, end):
    def rec(num):
        if num <= end:
            print(num)
            rec(num + 1)

    rec(start)


# task 3
numbers = [243, -279, 395, 130, 89, 269, 861, 669, 939, 367, -46, 710, 841, -280, -244, 274, -132, 273, 418, 432, -341,
           437, 360, 960, 195, 792, 106, 461, -35, 980, -80, 540, -358, 69, -26, -416, 597, 96, 533, 232, 755, 894, 331,
           323, -383, -386, 231, 436, 553, 967, 166, -151, 772, 434, 325, 301, 275, 431, 556, 728, 558, 702, 463, 127,
           984, 212, 876, -287, -16, -177, 577, 604, 116, 500, 653, 669, 916, 802, 817, 762, -210, -353, 144, -351, 777,
           805, 692, 22, -303, 249, 190, 411, 236, -274, 174, 380, 71, 124, -85, 430]


def print_list(lst):
    stop = len(lst)

    def rec(ind):
        if ind < stop:
            print(f"Элемент {ind}: {lst[ind]}")
            rec(ind + 1)

    rec(0)


# task 4
def print_reverse(numbers):
    stop = len(numbers)

    def rec(ind):
        if ind < stop:
            rec(ind + 1)
            print(numbers[ind])

    rec(0)


# task 5
def triangle(h):
    if h > 0:
        print(h*"*")
        triangle(h-1)


# task 6
def triangle(h):
    if h > 0:
        triangle(h-1)
        print(h*"*")


# task 7
def hourglass(threshold, neck=4):
    helper_list = [0, *range(threshold, 0, -1)]
    length = threshold*neck

    def rec(ind):
        if ind < threshold:
            print((f"{ind}"*neck*helper_list[ind]).center(length))
            rec(ind+1)
        print((f"{ind}"*neck*helper_list[ind]).center(length))
    rec(helper_list[-1])


# task 8
def print_digits(number):
    print(number % 10)
    if number > 10:
        print_digits(number // 10)


# task 9
def print_digits(number):
    if number > 10:
        print_digits(number // 10)
    print(number % 10)


# part 3

# task 1
def count(number):
    def rec(num, counter):
        if num//10:
            counter += 1
            return rec(num//10, counter)
        return counter + 1
    return rec(number, 0)


# task 3
number_of_frogs = lambda x: 77 if x == 1 else 3*(number_of_frogs(x-1)-30)

# task 4
range_sum = lambda lst, start, end: lst[start] if start >= end else lst[start] + range_sum(lst, start+1, end)

# task 5
get_pow = lambda a, n: 1 if not n else a* get_pow(a, n-1)

# task 6
def get_fast_pow(a, n):
    if not n:
        return 1
    elif not n%2:
        return get_fast_pow(a*a, n//2)
    else:
        return a*get_fast_pow(a, n-1)

# task 7
recursive_sum = lambda a, b: a if not b else 1 + recursive_sum(a, b-1)

# task 8
is_power = lambda x: x == 1 if x <= 1 else is_power(x / 2)

# task 9
def tribonacci(n):
    cache = {
        1: 1,
        2: 1,
        3: 1
    }

    def rec_trib(n):
        result = cache.get(n, 0)

        if not result:
            result = rec_trib(n - 1) + rec_trib(n - 2) + rec_trib(n - 3)
            cache[n] = result

        return result

    return rec_trib(n)

# without cache
def tribonacci(n, f1=1, f2=1, f3=1) -> int:
    if n == 1:
        return f1
    return tribonacci(n - 1, f2, f3, f1 + f2 + f3)

# task 10
def is_palindrome(string):
    if len(string) in (0, 1):
        return True

    if string[0] != string[-1]:
        return False

    return is_palindrome(string[1:-1])

# task 11
def to_binary(number):
    def rec_bin(num, result):
        if num not in (0, 1):
            result = [str(num % 2)] + result
            return rec_bin(num // 2, result)

        result = [str(num)] + result
        return "".join(result)

    return rec_bin(number, [])


# task 12
def without_cycles(number, subtrahend):
    if number > 0:
        print(number)
        without_cycles(number - subtrahend, subtrahend)
    print(number)


# part 4

# task 1
def recursive_sum(nested_lists):
    total = 0

    for item in nested_lists:
        if not isinstance(item, list):
            total += item
        else:
            total += recursive_sum(item)
    return total

def recursive_sum(nested_list: list) -> int:
    return sum((recursive_sum(el) if isinstance(el, list) else el for el in nested_list), start=0)


def recursive_sum(obj):
    if isinstance(obj, int):
        return obj
    return sum(map(recursive_sum, obj))


# task 2
def linear(nested_lists):
    result_list = []

    for item in nested_lists:
        result_list += [item] if isinstance(item, int) else linear(item)
    else:
        return result_list

# task 3
def get_value(nested_dicts, key):
    if key in nested_dicts:
        return nested_dicts[key]
    for k in nested_dicts.values():
        if isinstance(k, dict):
            res = get_value(k, key)
            if res:
                return res


# task 4
def get_all_values(nested_dict, key):
    result = set()

    if key in nested_dict:
        result.add(nested_dict[key])

    for item in nested_dict.values():
        if isinstance(item, dict):
            result |= get_all_values(item, key)

    return result

# task 5
def dict_travel(nested_dicts, path=None):
    for key, value in sorted(nested_dicts.items()):
        if not isinstance(value, dict):
            print(f"{path+'.'+str(key) if path else key}: {value}")
        else:
            dict_travel(nested_dicts[key], path=f"{path+'.'+str(key) if path else key}")




def main():
    print_hundred(1, 100)
    print_list(numbers)
    hourglass(4)


if __name__ == "main":
    main()
