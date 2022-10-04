from string import *
from random import sample


def generate_password(length):
    res = (set(ascii_letters) | set(digits)) - set('1Iilo0O')
    return ''.join(sample(list(res), length))


def generate_passwords(count, length):
    for i in range(count):
        print(generate_password(length))


n, m = int(input()), int(input())

generate_passwords(n, m)
