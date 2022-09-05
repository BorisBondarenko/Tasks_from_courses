n = int(input())

tmp = [input().split(' ') for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            tmp[i][j], tmp[n - i - 1][j] = tmp[n - i - 1][j], tmp[i][j]

for i in tmp:
    for j in i:
        print(j, end=' ')
    print()
