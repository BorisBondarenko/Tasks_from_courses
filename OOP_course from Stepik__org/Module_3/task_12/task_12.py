class DigitRetrieve:
    """This class describes the objects that make decision
    (could be value transform to int-type or not)"""

    def __call__(self, string, *args, **kwargs):
        for i in list(string if string[0] != '-' else string[1:]):
            if i.isalpha() or i in ('.', '-'):
                return None
        else:
            return int(string)


dg = DigitRetrieve()
st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]
