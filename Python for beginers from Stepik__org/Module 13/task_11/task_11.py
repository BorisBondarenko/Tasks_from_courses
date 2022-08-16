def merge(list1, list2):
    list1.extend(list2)
    list1.sort()
    return list1


numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

print(merge(numbers1, numbers2))
