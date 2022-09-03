x, y = input().split()
x = int(x)
y = int(y)

res = [[0 for j in range(y)] for i in range(x)]


def make_it_easy(matrix, counter):
    flag = True
    matrix.reverse()

    for i in range(x):
        if flag and 0 in matrix[i]:
            for j in range(y):
                if j < y and matrix[i][j] == 0:
                    matrix[i][j] = counter
                    counter += 1
            else:
                flag = False
                for r in range(len(matrix)):
                    matrix[r].reverse()
        elif not flag:
            for j in range(y):
                if matrix[i][j] == 0:
                    matrix[i][j] = counter
                    counter += 1
                    break

    finisher = ['try again' for row in matrix if 0 in row]

    if 'try again' in finisher:
        return make_it_easy(res, counter)
    else:
        if 1 in matrix[-1]:
            if matrix[-1][0] == 1:
                return matrix[::-1]
            else:
                for i in matrix:
                    i.reverse()
                return matrix[::-1]

        elif 1 in matrix[0]:
            if matrix[0][0] == 1:
                return matrix
            else:
                for i in matrix:
                    i.reverse()
                return matrix


for i in make_it_easy(res, 1):
    for j in i:
        print(str(j).ljust(3), end=' ')
    print()
