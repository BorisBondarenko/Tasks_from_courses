n = int(input())

tmp = [input().split(' ') for i in range(n)]
_1 = []
_2 = []
_3 = []
_4 = []

for i in range(n):
    for j in range(n):
        if j > i < n - 1 - j:
            _1.append(int(tmp[i][j]))
        elif j > i > n - 1 - j:
            _2.append(int(tmp[i][j]))
        elif j < i > n - 1 - j:
            _3.append(int(tmp[i][j]))
        elif j < i < n - 1 - j:
            _4.append(int(tmp[i][j]))

print(f'Верхняя четверть: {sum(_1)}')
print(f'Правая четверть: {sum(_2)}')
print(f'Нижняя четверть: {sum(_3)}')
print(f'Левая четверть: {sum(_4)}')
