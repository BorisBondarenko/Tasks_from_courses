n = int(input())

res = [[1 for j in range(1, i + 1)] for i in range(1, n + 2)]

for row in range(1, len(res)):
    for elem in range(len(res[row])):
        tmp = sum(res[row - 1][elem - 1:elem + 1])
        res[row][elem] = tmp if tmp else 1

print(res[-1])
