nums = input().split()

counter = 0
for i in set(nums):
    if nums.count(i) == 2:
        counter += 1
    elif nums.count(i) == 3:
        counter += 3
    elif nums.count(i) == 5:
        counter += 10

print(counter)
