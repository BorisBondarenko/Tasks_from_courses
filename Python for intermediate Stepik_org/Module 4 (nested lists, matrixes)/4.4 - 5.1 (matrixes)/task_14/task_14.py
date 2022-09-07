n = int(input())
m = int(input())

res = [[input() for j in range(m)] for i in range(n)]

for i in res:
    print(' '.join(i))

print()

for i in range(m):
    for j in range(n):
        print(res[j][i], end=' ')
    print()
