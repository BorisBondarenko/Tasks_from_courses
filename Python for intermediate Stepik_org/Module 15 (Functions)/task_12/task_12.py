from math import sqrt, sin

n = int(input())


def second_pow(number):
    return pow(number, 2)


def third_pow(number):
    return pow(number, 3)


def sqrt_num(number):
    return sqrt(number)


def abs_num(number):
    return abs(number)


def sin_num(number):
    return sin(number)


commands = {'квадрат': second_pow, 'куб': third_pow, 'корень': sqrt_num, 'модуль': abs_num, 'синус': sin_num}

print(commands[input()](n))
