def get_factors(num):
    return len([i for i in range(1, num + 1) if num % i == 0])


n = int(input())
print(get_factors(n))
