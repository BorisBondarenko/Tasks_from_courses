from random import shuffle

n = int(input())

first_part = [input() for i in range(n)]
second_part = first_part.copy()

while n:
    shuffle(first_part)
    shuffle(second_part)

    a = first_part.pop()
    b = second_part.pop()
    if a != b:
        print(f'{a}-{b}')
        n -= 1
    else:
        first_part.append(a)
        second_part.append(b)
