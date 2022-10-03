import random

length = int(input())

lower_case = [chr(i) for i in range(65, 90 + 1)]
upper_case = [chr(i) for i in range(97, 122 + 1)]

for i in range(length):
    print([lower_case, upper_case][random.randint(0, 1)][random.randint(0, len(lower_case))], end='')
