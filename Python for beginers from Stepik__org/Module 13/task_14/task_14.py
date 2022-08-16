def is_prime(num):
    if num == 1:
        return False
    else:
        res = [i for i in range(1, num + 1) if num % i == 0]
        return True if len(res) == 2 else False


n = int(input())
print(is_prime(n))
