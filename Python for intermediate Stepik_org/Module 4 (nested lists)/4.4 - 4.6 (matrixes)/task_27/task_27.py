x, y = input()
x = ord(x) - 96
y = int(y)

a = (-2, -1, 1, 2)
rel = [[x + i, 8 - y + j + 1] for j in a for i in a if abs(i) != abs(j)]

tmp = [['.' for j in range(8)] for i in range(8)]
tmp[8 - y][x - 1] = 'N'

for i in range(8):
    for j in range(8):
        print('*' if [j + 1, i + 1] in rel else tmp[i][j], end=' ')
    print()
