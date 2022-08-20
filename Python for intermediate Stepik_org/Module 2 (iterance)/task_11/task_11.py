nums = input().split()

for i in range(0, len(nums), 2):
    if len(nums) % 2 == 0:
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
    else:
        nums.append('x')
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
    if nums[-2] == 'x':
        del nums[-2]

for i in nums:
    print(i, end=' ')
