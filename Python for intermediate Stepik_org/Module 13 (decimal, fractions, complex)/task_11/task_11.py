from fractions import Fraction

n = int(input())

tmp = []
for b in range(1, n + 1):
    for a in range(1, n + 1):
        if Fraction(a, b).numerator + Fraction(a, b).denominator == n and a < b:
            tmp.append(Fraction(a, b))
print(sorted(tmp, key=lambda x: x.numerator, reverse=True)[0])
