from math import pow, sqrt


def solve(a, b, c):
    x1 = (-b - sqrt(pow(b, 2) - (4 * a * c))) / (2 * a)
    x2 = (-b + sqrt(pow(b, 2) - (4 * a * c))) / (2 * a)

    res = [x1, x2]
    res.sort()

    return res


a, b, c = int(input()), int(input()), int(input())
x1, x2 = solve(a, b, c)
print(x1, x2)
