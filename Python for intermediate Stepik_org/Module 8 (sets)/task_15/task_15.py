phr_1 = set([int(i) for i in input().split()])
phr_2 = set([int(i) for i in input().split()])

print(*sorted(phr_1.intersection(phr_2)), end=' ')
