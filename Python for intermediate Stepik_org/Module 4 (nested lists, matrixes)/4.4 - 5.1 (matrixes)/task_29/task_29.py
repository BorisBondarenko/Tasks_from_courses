x, y = input().split()
x = int(x)
y = int(y)

tmp_1, tmp_2 = True, False

res = []
for i in range(100):
    _ = []
    for j in range(100):
        tmp_1, tmp_2 = tmp_2, tmp_1
        _.append('*' if tmp_1 else '.')
    res.append(_)
    tmp_1, tmp_2 = tmp_2, tmp_1

for i in range(x):
    for j in range(y):
        print(res[i][j], end=' ')
    print()
