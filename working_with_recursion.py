def print_numbers(start, end):
    def rec(num):
        if num <= end:
            print(num)
            rec(num + 1)
    rec(start)


print(print_numbers(0, 10))
