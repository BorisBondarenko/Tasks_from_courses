class TupleLimit(tuple):

    def __new__(cls, a, b):
        return super(TupleLimit, cls).__new__(cls, tuple(a))

    def __init__(self, lst, max_length):
        if len(lst) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')
        else:
            self.lst = lst

    def __str__(self):
        return ' '.join(map(str, self.lst))

    def __repr__(self):
        return ' '.join(map(str, self.lst))


digits = list(map(float, input().split()))

try:
    tup = TupleLimit(digits, 5)
except Exception as e:
    print(e)
else:
    print(tup)
