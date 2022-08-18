lst_in = input().split()


def int_maker(value):
    try:
        return int(value)
    except ValueError:
        return False


res = sum(filter(bool, map(lambda x: int_maker(x), lst_in)))
print(res)
