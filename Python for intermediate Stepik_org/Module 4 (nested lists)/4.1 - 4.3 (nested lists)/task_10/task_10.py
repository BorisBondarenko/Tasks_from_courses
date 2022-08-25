n = input().split()
res = [[]]
tmp = []

for i in n:
    if i not in res[-1]:
        tmp.append(i)
        res.append(tmp)
    else:
        res[-1].append(i)
    tmp = []

print(res[1:])
