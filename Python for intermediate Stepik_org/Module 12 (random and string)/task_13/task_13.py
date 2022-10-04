from string import *
from random import shuffle, randint


def generate_password(length):
    upper_c = list(set(ascii_uppercase) - set('IO'))
    lower_c = list(set(ascii_lowercase) - set('ilo'))
    digit_c = list(set(digits) - set('10'))
    all_c = [upper_c, lower_c, digit_c]

    res = []
    for i in range(length):
        shuffle(all_c)
        from_all = all_c[randint(0, len(all_c) - 1)]
        res.append(str(from_all[randint(0, len(from_all) - 1)]))

    res[0] = upper_c[randint(0, len(upper_c) - 1)]
    res[-1] = lower_c[randint(0, len(lower_c) - 1)]
    res[1] = digit_c[randint(0, len(digit_c) - 1)]

    return ''.join(res)


def generate_passwords(count, length):
    for i in range(count):
        print(generate_password(length))


n, m = int(input()), int(input())
generate_passwords(n, m)
