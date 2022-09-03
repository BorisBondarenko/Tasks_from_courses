x, y = input().split()
x = int(x)
y = int(y)

tmp = [i if i < x else x for i in range(1, y)]
tmp_2 = [i for i in range(x - 1, 0, -1)]
tmp = tmp + tmp_2 if y != 2 else tmp * x

i_s = []
counter = 0
row_grow = 1
while len(i_s) < x:
    r = 0
    if y > 2:
        i_s.append(counter + row_grow + r)
    elif y == 1:
        i_s.append(counter + 1)
    elif y == 2 and counter % 2 != 0:
        i_s.append(counter)
    row_grow += counter + 1
    counter += 1

for i in range(x):
    res = i_s[i]
    for j in range(y):
        if res != x * y:
            print(str(res).ljust(3), end=' ')
            res += tmp[i:i + y + 1][j]
        else:
            print(str(res).ljust(3), end=' ')
            break
    print()
