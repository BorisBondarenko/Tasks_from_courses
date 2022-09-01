n = int(input())
m = int(input())

tmp = [[int(j) for j in input().split(' ')] for i in range(n)]

max_ = -1000
for i in range(n):
    for j in range(m):
        if tmp[i][j] >= max_:
            max_ = tmp[i][j]

res = []
for i in range(n):
    for j in range(m):
        if tmp[i][j] == max_:
            res.append(f'{i} {j}')

print(res[0])
