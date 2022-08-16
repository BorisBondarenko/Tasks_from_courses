def is_valid_password(password):
    if len(password.split(':')) == 3:
        a, b, c = password.split(':')
    else:
        return False

    res = [i for i in range(1, int(b) + 1) if int(b) % i == 0]

    is_poli = True if a == a[::-1] else False
    is_even = True if int(c) % 2 == 0 else False
    is_simple = True if len(res) == 2 else False

    return True if is_poli and is_simple and is_even else False


psw = input()
print(is_valid_password(psw))
