n = int(input())

mat = []
for i in range(n):
    mat.append(input().split())

z = int(input()) - 1


def make_it_easy(mat_1, mat_2, step_to_end):
    res_matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            counter = 0
            for m in range(n):
                counter += int(mat_1[i][m]) * int(mat_2[m][j])
            row.append(counter)
        res_matrix.append(row)
    step_to_end -= 1
    if step_to_end > 0:
        return make_it_easy(mat_1, res_matrix, step_to_end)
    elif step_to_end == 0:
        return res_matrix


for i in make_it_easy(mat, mat, z):
    for j in i:
        print(str(j).ljust(3), end=' ')
    print()
