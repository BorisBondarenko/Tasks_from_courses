x, y = input()
x = ord(x) - 96 - 1
y = int(y) - 1

tmp = [['.' for j in range(8)] for i in range(8)]
tmp[y][x] = 'Q'

for i in range(8):
    for j in range(8):
        if abs(x - i) == abs(y - j) or x == i or y == j:
            tmp[j][i] = '*' if tmp[j][i] != 'Q' else 'Q'

tmp = tmp[::-1]
for i in range(8):
    for j in range(8):
        print(tmp[i][j], end=' ')
    print()
