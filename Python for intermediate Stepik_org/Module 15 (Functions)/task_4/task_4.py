def mean(*args):
    res = [i for i in args if type(i) == int or type(i) == float]
    if res:
        return sum(res) / len(res)
    else:
        return float(0)
