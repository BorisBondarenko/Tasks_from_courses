class Vector:
    def __init__(self, *args):
        self.coords = args

    @staticmethod
    def checker(self_value, value):
        if len(self_value) != len(value):
            raise ArithmeticError('размерности векторов не совпадают')
        return True

    def __add__(self, other):
        if isinstance(other, Vector):
            self.checker(self.coords, other.coords)
            return Vector(*list(map(sum, zip(self.coords, other.coords))))
        elif isinstance(other, int):
            return Vector(*list(map(lambda x: x + other, self.coords)))

    def __iadd__(self, other):
        if isinstance(other, Vector):
            self.checker(self.coords, other.coords)
            self.coords = tuple(map(sum, zip(self.coords, other.coords)))
        elif isinstance(other, int):
            self.coords = tuple(map(lambda x: x + other, self.coords))
        return self

    def __sub__(self, other):
        if isinstance(other, Vector):
            self.checker(self.coords, other.coords)
            return Vector(*list(map(lambda x: x[0] - x[-1], zip(self.coords, other.coords))))
        elif isinstance(other, int):
            return Vector(*list(map(lambda x: x - other, self.coords)))

    def __isub__(self, other):
        if isinstance(other, Vector):
            self.checker(self.coords, other.coords)
            self.coords = tuple(map(lambda x: x[0] - x[-1], zip(self.coords, other.coords)))
        elif isinstance(other, int):
            self.coords = tuple(map(lambda x: x - other, self.coords))
        return self

    def __mul__(self, other):
        if isinstance(other, Vector):
            self.checker(self.coords, other.coords)
            return Vector(*list(map(lambda x: x[0] * x[-1], zip(self.coords, other.coords))))
        elif isinstance(other, int):
            return Vector(*list(map(lambda x: x * other, self.coords)))

    def __imul__(self, other):
        if isinstance(other, Vector):
            self.checker(self.coords, other.coords)
            self.coords = tuple(map(lambda x: x[0] * x[-1], zip(self.coords, other.coords)))
        elif isinstance(other, int):
            self.coords = tuple(map(lambda x: x * other, self.coords))
        return self

    def __eq__(self, other):
        self.checker(self.coords, other.coords)
        return all(map(lambda x: x[0] == x[-1], zip(self.coords, other.coords)))