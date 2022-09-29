phr = input().split(' ')

res = {}
for i in phr:
    if i not in res:
        res[i] = 1
        print(res[i], end=' ')
    else:
        res[i] += 1
        print(res[i], end=' ')
