x, y = input().split()
x = int(x)
y = int(y)

tmp = []
total = 1
for i in range(y):
    _ = []
    for j in range(x):
        _.append(str(total).ljust(3))
        total += 1
    tmp.append(_)

for i in range(x):
    for j in range(y):
        print(tmp[j][i], end=' ')
    print()
