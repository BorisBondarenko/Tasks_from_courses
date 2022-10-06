from fractions import Fraction

n = int(input())

res = 0
for i in range(1, n + 1):
    res += Fraction(1, pow(i, 2))

print(res)
