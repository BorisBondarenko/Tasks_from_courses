class Vector:
    _allowed_types = (int, float)

    def __new__(cls, *args, **kwargs):
        if not cls.__is_allowed(args):
            raise ValueError('координаты должны быть целыми или вещественными числами')
        return object.__new__(cls)

    def __init__(self, *args):
        self.coords = tuple(args)

    @classmethod
    def __is_allowed(cls, instance):
        return all(map(lambda x: type(x) in cls._allowed_types, instance))

    def len_checker(self, other):
        if len(self.get_coords()) != len(other.get_coords()):
            raise TypeError('размерности векторов не совпадают')
        return True

    def get_coords(self):
        return self.coords

    def __add__(self, other):
        self.len_checker(other)
        res = list(map(lambda x: x[0] + x[1], zip(self.get_coords(), other.get_coords())))
        return self.__class__(*res) if self.__is_allowed(res) else Vector(*res)

    def __sub__(self, other):
        self.len_checker(other)
        res = list(map(lambda x: x[0] - x[1], zip(self.get_coords(), other.get_coords())))
        return self.__class__(*res) if self.__is_allowed(res) else Vector(*res)


class VectorInt(Vector):
    _allowed_types = (int,)