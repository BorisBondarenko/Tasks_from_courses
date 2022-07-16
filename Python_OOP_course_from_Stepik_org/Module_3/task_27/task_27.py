class NewList:
    """This class describes the new model of lists.
    By using this type of lists you have the opportunity to
    do subtraction operations like you already do this with int-type"""

    def __init__(self, lst=None):
        self.lst = lst if lst else []

    def get_list(self):
        return self.lst

    def make_it_easy(self, inner, other):
        """The main method to make what that class should be able to."""

        inner = list(map(lambda x: str(x), inner.lst))
        other = list(map(lambda x: str(x), other.lst))

        res = '|'.join(inner)

        for i in set(other):
            if i in inner:
                res = res.replace(i, '___', other.count(i))

        res = list(filter(lambda x: x != '', res.replace('___', '').split('|')))

        for i in range(len(res)):
            if res[i].isdigit() or '-' in res and '.' not in res[i]:
                res[i] = int(res[i])
            elif '.' in res[i]:
                res[i] = float(res[i])
            elif res[i] == 'False':
                res[i] = False
            elif res[i] == 'True':
                res[i] = True
            elif res[i].isalpha():
                continue
        return res

    def __sub__(self, other):
        if type(other) == list:
            return NewList(self.make_it_easy(self, NewList(other)))
        return NewList(self.make_it_easy(self, other))

    def __rsub__(self, other):
        if type(other) == list:
            return NewList(other) - self
        return other - self

    def __isub__(self, other):
        if type(other) == list:
            other = NewList(other)
        self.lst = self.make_it_easy(self, other)
        return self
