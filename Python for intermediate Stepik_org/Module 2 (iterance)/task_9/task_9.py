n = int(input())

res = {i: [] for i in range(1, 5)}

for i in range(n):
    x, y = input().split()
    if int(x) > 0 and int(y) > 0:
        res[1].append(1)
    elif int(x) < 0 and int(y) > 0:
        res[2].append(1)
    elif int(x) < 0 and int(y) < 0:
        res[3].append(1)
    elif int(x) > 0 and int(y) < 0:
        res[4].append(1)

print(f'Первая четверть: {len(res[1])}')
print(f'Вторая четверть: {len(res[2])}')
print(f'Третья четверть: {len(res[3])}')
print(f'Четвертая четверть: {len(res[4])}')