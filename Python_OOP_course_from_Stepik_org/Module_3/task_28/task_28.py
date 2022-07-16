class ListMath:
    """This class describes the new type of list as an object.
    With the objects of this class (lists) to can make all arithmetic operations,
    as you usually doing with int-objects."""

    def __init__(self, lst=None):
        self.lst_math = [] if not lst else lst
        self.lst_math = list(filter(lambda x: type(x) in (float, int), lst))

        # ___________________________________________

    def __add__(self, other):
        return ListMath([i + other for i in self.lst_math])

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.lst_math = [i + other for i in self.lst_math]
        return self

    # ___________________________________________
    def __sub__(self, other):
        return ListMath([i - other for i in self.lst_math])

    def __rsub__(self, other):
        return ListMath([other - i for i in self.lst_math])

    def __isub__(self, other):
        self.lst_math = [i - other for i in self.lst_math]
        return self

    # ___________________________________________

    def __mul__(self, other):
        return ListMath([i * other for i in self.lst_math])

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self.lst_math = [i * other for i in self.lst_math]
        return self

    # ___________________________________________

    def __truediv__(self, other):
        return ListMath([i / other for i in self.lst_math])

    def __rtruediv__(self, other):
        return ListMath([other / i for i in self.lst_math])

    def __itruediv__(self, other):
        self.lst_math = [i / other for i in self.lst_math]
        return self
