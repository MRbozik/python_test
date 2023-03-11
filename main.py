import time

from functools import wraps


def decarate(func):
    @wraps(func)
    def inner(*args, **kwargs):
        s = time.time()
        print("Start time")
        func(*args, **kwargs)
        print("Finish time")
        time.sleep(2)
        e = time.time()
        print(e - s)

    return inner


@decarate
def show(*args):
    print("Check", *args)


class Person:
    def __init__(self, name, lastname, years):
        self.__name = name
        self.__lastname = lastname
        self.__years = years

    @property
    def reg(self):
        return self.__name,

    @reg.setter
    def reg(self, name, lastname, year):
        self.__name = name
        self.__lastname = lastname
        self.__years = year


if __name__ == '__main__':
    show(34)
