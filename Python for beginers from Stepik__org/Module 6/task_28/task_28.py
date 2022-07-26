x, y, act = int(input()), int(input()), input()

if act == '+':
    print(x + y)
elif act == '-':
    print(x - y)
elif act == '*':
    print(x * y)
elif act == '/':
    if y == 0:
        print('На ноль делить нельзя!')
    else:
        print(x / y)
else:
    print('Неверная операция')
