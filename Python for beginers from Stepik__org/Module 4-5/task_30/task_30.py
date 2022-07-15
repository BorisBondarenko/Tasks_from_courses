num = int(input())

if 1 <= num <= 10:
    if 1 <= num <= 3:
        print('I' * num)
    elif 4 <= num <= 8:
        if num % 5 == 0:
            print('V')
        elif num % 5 == num:
            print('IV')
        elif num % 5 > 0:
            print(f'V{"I" * (num % 5)}')

    elif 9 <= num <= 10:
        if num % 10 == 0:
            print('X')
        elif num % 10 == num:
            print('IX')
else:
    print('ошибка')