n = int(input())

for i in range(n):
    for j in range(n):
        if i < n - 1 - j:
            print('0', end=' ')
        elif j == n - i - 1:
            print('1', end=' ')
        elif i > n - 1 - j:
            print('2', end=' ')
    print()
