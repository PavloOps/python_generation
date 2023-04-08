import pickle
import sys


def task1():
    dogs = {'Ozzy': 2, 'Filou': 7, 'Luna': 4, 'Skippy': 11, 'Barco': 13, 'Balou': 10, 'Laika': 15}

    with open('dogs.pkl', mode='wb') as file:
        pickle.dump(dogs, file)


def task2():
    file_name = input()
    arguments = (i.strip() for i in sys.stdin)

    with open(file_name, mode="rb") as binary_file:
        lonely_func = pickle.load(binary_file)
        print(lonely_func(*arguments))


def task3():
    def filter_dump(filename, objects, typename):
        with open(filename, mode="wb") as binary_file:
            obj = list(i for i in objects if type(i) == typename)
            pickle.dump(obj, binary_file)


def task4():
    file_name, check_sum = input(), int(input())

    with open(file_name, mode="rb") as binary_file:
        obj = pickle.load(binary_file)
        lst = [i for i in obj if type(i) == int] or [0]
        res = sum(lst) if type(obj) == dict else max(lst) * min(lst)

    print(['Контрольные суммы не совпадают', 'Контрольные суммы совпадают'][check_sum == res])
