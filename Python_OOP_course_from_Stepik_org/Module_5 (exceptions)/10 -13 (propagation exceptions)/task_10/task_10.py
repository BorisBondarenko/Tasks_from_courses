def input_int_numbers():
    try:
        values = map(int, input().split())
    except ValueError:
        raise ValueError('все числа должны быть целыми')
    return tuple(values)


switcher = False

while not switcher:
    try:
        res = input_int_numbers()
    except ValueError:
        continue
    else:
        switcher = True
        print(*res)
