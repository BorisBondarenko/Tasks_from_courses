from fractions import Fraction

n = int(input())
tmp = []

for b in range(1, n + 1):
    for a in range(1, n + 1):
        if a < b:
            tmp.append(Fraction(a, b))

for i in sorted(set(tmp)):
    print(i)
