from fractions import Fraction
from math import factorial

n = int(input())

res = 0
for i in range(1, n + 1):
    res += Fraction(1, factorial(i))

print(res)
