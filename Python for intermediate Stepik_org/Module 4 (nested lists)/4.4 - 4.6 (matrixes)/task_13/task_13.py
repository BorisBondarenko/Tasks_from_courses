n = int(input())
m = int(input())

res = [[input() for j in range(m)] for i in range(n)]

for k in res:
    print(' '.join(k))
