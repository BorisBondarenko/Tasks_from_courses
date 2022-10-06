from fractions import Fraction

a = input()
b = input()

print(f'{a} + {b} = {Fraction(a) + Fraction(b)}')
print(f'{a} - {b} = {Fraction(a) - Fraction(b)}')
print(f'{a} * {b} = {Fraction(a) * Fraction(b)}')
print(f'{a} / {b} = {Fraction(a) / Fraction(b)}')
