x, y = input().split()
x_1 = int(x)
y_1 = int(y)

mat_1 = []
for i in range(x_1):
    mat_1.append(input().split())

input()

x, y = input().split()
x_2 = int(x)
y_2 = int(y)

mat_2 = []
for i in range(x_2):
    mat_2.append(input().split())

res_matrix = []
for i in range(x_1):
    row = []
    for j in range(y_2):
        counter = 0
        for m in range(x_2):
            counter += int(mat_1[i][m]) * int(mat_2[m][j])
        row.append(counter)
    res_matrix.append(row)

for i in res_matrix:
    for j in i:
        print(str(j).ljust(3), end=' ')
    print()
