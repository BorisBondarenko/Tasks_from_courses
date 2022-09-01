n = int(input())

tmp = [input().split(' ') for i in range(n)]

answer = True
for i in range(n):
    for j in range(n):
        if tmp[i][j] != tmp[j][i]:
            answer = False

print('YES' if answer else 'NO')
