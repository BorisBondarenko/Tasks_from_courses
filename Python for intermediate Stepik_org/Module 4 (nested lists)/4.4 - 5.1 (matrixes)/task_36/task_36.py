x, y = input().split()
x = int(x)
y = int(y)

total = 1
for i in range(x):
    if i % 2 == 0:
        for j in range(y):
            print(str(total).ljust(3), end=' ')
            total += 1
        print()
    elif i % 2 != 0:
        for j in range(y):
            print(str(total + y - j - 1).ljust(3), end=' ')
        total += y
        print()
