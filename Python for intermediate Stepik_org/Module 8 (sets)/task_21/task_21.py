set_1 = set(map(int, input().split(' ')))
set_2 = set(map(int, input().split(' ')))
set_3 = set(map(int, input().split(' ')))

full = set_1 | set_2 | set_3
center = set_1 & set_2 & set_3
print(*sorted(full.difference(center), reverse=False))
