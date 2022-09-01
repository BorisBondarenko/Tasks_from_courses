n = int(input())

tmp = [input().split(' ') for i in range(n)][::-1]

for i in range(n):
    for j in range(n):
        print(tmp[j][i], end=' ')
    print()
