n = int(input())

tmp = [input().split(' ') for i in range(n)]
tmp_2 = [[tmp[abs(j)][abs(i)] for j in range(-n + 1, 1)] for i in range(-n + 1, 1)]

answer = True
for i in range(n):
    for j in range(n):
        if i < n - 1 - j:
            if tmp[i][j] != tmp_2[i][j]:
                answer = False

print('YES' if answer else 'NO')
