n = int(input())

tmp = [input().split(' ') for i in range(n)]
res = []
for i in range(n):
    for j in range(n):
        if j <= i <= n - 1 - j:
            res.append(int(tmp[i][j]))
        elif j >= i >= n - 1 - j:
            res.append(int(tmp[i][j]))

print(max(res))
