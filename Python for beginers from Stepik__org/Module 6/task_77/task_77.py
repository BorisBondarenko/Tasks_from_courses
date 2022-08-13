n = int(input()[1:])

res = []
for i in range(n):
    phr = input().split('#')[0]
    res.append(phr.rstrip())

for k in res:
    print(k)
