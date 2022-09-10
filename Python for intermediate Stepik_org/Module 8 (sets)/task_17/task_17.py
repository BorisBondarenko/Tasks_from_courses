n = int(input())

num = set(list(input()))
for i in range(n - 1):
    num.intersection_update(set(list(input())))

print(*sorted(num), end=' ')
