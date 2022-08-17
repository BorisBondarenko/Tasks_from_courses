from math import factorial


def compute_binom(n, k):
    a = factorial(n)
    b = factorial(k)
    c = factorial(n - k)

    return int(a / (b * c))


n = int(input())
k = int(input())

print(compute_binom(n, k))
