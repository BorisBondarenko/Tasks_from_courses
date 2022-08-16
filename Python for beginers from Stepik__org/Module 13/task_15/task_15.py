def get_next_prime(num):
    for x in range(num, 1000):
        res = [i for i in range(1, x + 1) if x % i == 0]
        if len(res) == 2 and x > num:
            return x


n = int(input())
print(get_next_prime(n))
