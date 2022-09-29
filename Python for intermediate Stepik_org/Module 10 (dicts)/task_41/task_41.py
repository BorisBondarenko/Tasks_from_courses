n = int(input())

res = {}
for i in range(n):
    buyer, product, amount = input().split(' ')
    if buyer not in res:
        res[buyer] = {}
        res[buyer] = dict(zip([product], [int(amount)]))
    else:
        if product not in res[buyer]:
            res[buyer].update(dict(zip([product], [int(amount)])))
        else:
            res[buyer][product] += int(amount)

for i in sorted(res):
    print(f'{i}:')
    for k, v in sorted(res[i].items()):
        print(k, v, sep=' ')
