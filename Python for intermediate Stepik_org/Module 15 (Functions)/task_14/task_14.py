nums = input().split(' ')


def sum_digits(str_x):
    return sum([int(i) for i in str_x])


print(*sorted(nums, key=lambda x: (sum_digits(x), int(x))))
