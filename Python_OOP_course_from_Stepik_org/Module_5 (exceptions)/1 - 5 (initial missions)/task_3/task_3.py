lst_in = input().split()


def type_changer(value):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except Exception:
            return value


lst_out = list(map(lambda x: type_changer(x), lst_in))
