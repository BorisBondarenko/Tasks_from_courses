n = int(input())

matrix = [input().split(' ') for i in range(n)]

nums = []
for i in range(n):
    for j in range(n):
        if i > (n - 1 - j) or (i + 1 + j) == n:
            nums.append(matrix[i][j])

print(max(nums))
