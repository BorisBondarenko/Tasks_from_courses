n = int(input())
m = int(input())

res = [[str(i * j) for j in range(m)] for i in range(n)]

for i in res:
    print(' '.join(i))
