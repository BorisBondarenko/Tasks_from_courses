list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
max_ = -1

for li in list1:
    for i in li:
        if i >= max_:
            max_ = i

print(max_)
