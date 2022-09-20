phr = input().lower()

counting = {}

for i in phr.split(' '):
    if i not in counting:
        print(i, end=' ')
        counting[i] = 1
    else:
        print(f'{i}_{counting[i]}', end=' ')
        counting[i] += 1
