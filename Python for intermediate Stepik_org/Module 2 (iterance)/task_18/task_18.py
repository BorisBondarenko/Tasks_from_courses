n = int(input())
res = []

for i in range(n):
    phr = input()
    rest = ['a', 'n', 't', 'o', 'n']
    anton = ''
    for j in phr:
        if j == rest[0]:
            anton += rest.pop(0)
        if len(rest) == 0:
            break
        else:
            continue

    if anton == 'anton':
        res.append(i + 1)

for r in res:
    print(r, end=' ')
