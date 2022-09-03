x, y = input().split()
x = int(x)
y = int(y)

matrix_1 = []
for i in range(x):
    matrix_1.append(input().split())

input()

matrix_2 = []
for i in range(x):
    matrix_2.append(input().split())

res_matrix = []
for i in range(x):
    row = []
    for j in range(y):
        row.append(int(matrix_1[i][j]) + int(matrix_2[i][j]))
    res_matrix.append(row)

for i in res_matrix:
    for j in i:
        print(str(j).ljust(3), end=' ')
    print()
