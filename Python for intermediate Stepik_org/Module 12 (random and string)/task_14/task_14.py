import random

n = 10 ** 6  # количество испытаний
k = 0
So = 16

for i in range(n):
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)
    if pow(x, 3) + pow(y, 4) + 2 >= 0 and 3 * x + pow(y, 2) <= 2:
        k += 1

print((k / n) * So)
