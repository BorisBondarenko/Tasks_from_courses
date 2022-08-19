nums = input().split()
res = []
for i in range(1, len(nums)):
    if int(nums[i]) > int(nums[i - 1]):
        res.append(i)
    else:
        continue

print(len(res))
