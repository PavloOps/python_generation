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


def main():
    print(print_hundred(1, 100))


if __name__ == "main":
    main()
