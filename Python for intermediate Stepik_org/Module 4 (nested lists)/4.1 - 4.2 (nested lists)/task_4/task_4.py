list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]

for i in range(len(list1)):
    x = list1.pop(i)
    list1.insert(i, x[::-1])

print(list1)
