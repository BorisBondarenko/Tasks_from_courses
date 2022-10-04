from random import sample, shuffle

nums = [i for i in range(1, 75 + 1)]

matrix = []
for i in range(5):
    row = []
    for j in range(5):
        shuffle(nums)
        row.append(nums.pop())
    matrix.append(row)
matrix[2][2] = 0

for i in matrix:
    print(*i)
