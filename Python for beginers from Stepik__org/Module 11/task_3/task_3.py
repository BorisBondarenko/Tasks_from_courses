n = input().split(' ')
res = ''
for i in n:
    res += str(i) + "+"

total = sum([int(i) for i in n])
print(f'{res[:-1]}={total}')
