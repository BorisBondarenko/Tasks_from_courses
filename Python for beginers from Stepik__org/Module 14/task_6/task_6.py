def is_magic(date):
    d, m, y = date.split('.')
    if int(d) * int(m) == int(y[2:]):
        return True
    else:
        return False


date = input()
print(is_magic(date))
