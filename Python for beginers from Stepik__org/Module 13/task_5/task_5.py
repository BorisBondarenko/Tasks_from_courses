def print_digit_sum(num):
    res = sum([int(i) for i in str(num)])
    print(res)


n = int(input())
print_digit_sum(n)
