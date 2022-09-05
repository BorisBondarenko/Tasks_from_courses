phr = input().replace(' ', '')
n = int(input())

res = []
for j in range(n):
    row = [phr[i] for i in range(j, len(phr), n)]
    res.append(row)

print(res)
