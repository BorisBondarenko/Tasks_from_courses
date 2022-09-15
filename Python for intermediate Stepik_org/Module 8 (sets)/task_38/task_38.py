my_set1 = {i for i in input().split(" ")}
my_set2 = {i for i in input().split(" ")}

res = sorted(my_set1 | my_set2)
print(*res)
