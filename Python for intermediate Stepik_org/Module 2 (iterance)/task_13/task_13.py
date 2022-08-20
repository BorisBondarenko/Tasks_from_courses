nums = input().split()
nums.insert(0, nums.pop(-1))
for i in nums:
    print(i, end=' ')
