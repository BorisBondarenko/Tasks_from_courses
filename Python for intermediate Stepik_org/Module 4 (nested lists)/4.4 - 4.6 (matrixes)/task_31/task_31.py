x, y = input().split()
x = int(x)
y = int(y)

total = 1
for i in range(x):
    for j in range(y):
        print(str(total).ljust(3), end=' ')
        total += 1
    print()
