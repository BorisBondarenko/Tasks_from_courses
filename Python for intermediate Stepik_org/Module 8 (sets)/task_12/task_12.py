phr = input().lower()

for i in '.,;:-?!':
    phr = phr.replace(i, '')

print(len(set([i for i in phr.split()])))
