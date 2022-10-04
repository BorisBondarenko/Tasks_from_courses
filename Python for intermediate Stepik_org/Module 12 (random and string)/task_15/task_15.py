import random

n = 10 ** 6
k = 0
So = 4

for i in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if pow(x, 2) + pow(y, 2) <= 1:
        k += 1

print((k / n) * So)
