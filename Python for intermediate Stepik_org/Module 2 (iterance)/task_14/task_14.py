n = int(input())
nums = [int(input()) for i in range(n)]
x = int(input())

answer = False
for i in range(len(nums)):
    for j in range(len(nums)):
        if j == i:
            continue
        if nums[i] * nums[j] == x:
            answer = True

print('ДА' if answer and n > 1 else 'НЕТ')
