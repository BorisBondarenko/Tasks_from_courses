n = int(input())

for i in range(n):
    for j in range(n):
        if i == j:
            print('*', end=' ')
        elif j == n - i - 1:
            print('*', end=' ')
        elif i == (n // 2) or j == (n // 2):
            print('*', end=' ')
        else:
            print('.', end=' ')
    print()
