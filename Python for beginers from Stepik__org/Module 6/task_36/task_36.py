num = int(input())

if num % 2 != 0:
    print('YES')
else:
    if 2 <= num <= 5:
        print('NO')
    elif 6 <= num <= 20:
        print('YES')
    elif num > 20:
        print('NO')
