import random

n = int(input())

for i in range(n):
    print(['Орел', 'Решка'][random.randint(0, 1)])
