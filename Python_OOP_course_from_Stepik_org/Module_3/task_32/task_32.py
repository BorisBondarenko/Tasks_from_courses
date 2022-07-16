from _operator import floordiv
from operator import add, sub, mul, mod


class Box3D:
    """This class describes 3D Box objects with attributes (width, height, depth)
    and arithmetic operations to manage them as if this is the int-objects"""

    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    @staticmethod
    def calc(a, b, func):
        if isinstance(b, Box3D):
            new_width = func(a.width, b.width)
            new_height = func(a.height, b.height)
            new_depth = func(a.depth, b.depth)
            return new_width, new_height, new_depth

        elif isinstance(b, int or float):
            new_width = func(a.width, b)
            new_height = func(a.height, b)
            new_depth = func(a.depth, b)
            return new_width, new_height, new_depth

    def __add__(self, other):
        return Box3D(*self.calc(self, other, add))

    def __radd__(self, other):
        return self + other

    # ________________________________________

    def __sub__(self, other):
        return Box3D(*self.calc(self, other, sub))

    def __rsub__(self, other):
        return self - other

    # ________________________________________

    def __mul__(self, other):
        return Box3D(*self.calc(self, other, mul))

    def __rmul__(self, other):
        return self * other

    # ________________________________________

    def __floordiv__(self, other):
        return Box3D(*self.calc(self, other, floordiv))

    def __rfloordiv__(self, other):
        return self // other

    # ________________________________________

    def __mod__(self, other):
        return Box3D(*self.calc(self, other, mod))

    def __rmod__(self, other):
        return self % other