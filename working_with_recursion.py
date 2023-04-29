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


def main():
    print_hundred(1, 100)
    print_list(numbers)
    hourglass(4)


if __name__ == "main":
    main()
