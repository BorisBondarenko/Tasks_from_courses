from math import pi


def get_circle(radius):
    c = 2 * pi * radius
    s = pi * radius ** 2
    return c, s


r = float(input())

length, square = get_circle(r)
print(length, square)
