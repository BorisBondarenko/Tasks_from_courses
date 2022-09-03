n = int(input())

matrix = [input().split(' ') for i in range(n)]

for i in range(n):
    for j in range(n):
        print(matrix[j][i], end=' ')
    print()
