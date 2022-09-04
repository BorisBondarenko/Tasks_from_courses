n = int(input())

tmp = [i for i in range(n)]
tmp = tmp[::-1] + tmp[1:]

matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(tmp[abs(n - 1 - i):][j])
    matrix.append(row)

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()
