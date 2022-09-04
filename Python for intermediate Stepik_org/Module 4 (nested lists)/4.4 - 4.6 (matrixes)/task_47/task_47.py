n = int(input())

tmp_1 = [input().split(' ') for i in range(n)]

tmp_2 = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(tmp_1[::-1][j][i])
    tmp_2.append(row)

answer = True
for x in range(1, n + 1):
    for i in range(n):
        if not tmp_1[i].count(str(x)):
            answer = False
        if not tmp_2[i].count(str(x)):
            answer = False

print('YES' if answer else 'NO')
