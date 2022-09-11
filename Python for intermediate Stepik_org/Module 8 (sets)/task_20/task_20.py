first = set(map(int, input().split(' ')))
second = set(map(int, input().split(' ')))
third = set(map(int, input().split(' ')))

print(*sorted(first.intersection(second).difference(third), reverse=True))
