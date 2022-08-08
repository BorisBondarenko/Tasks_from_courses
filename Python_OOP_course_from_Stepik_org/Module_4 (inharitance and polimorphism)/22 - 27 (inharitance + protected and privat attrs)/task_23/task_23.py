class Furniture:
    """This class describes the furniture in general.
    This class using as parent class for more specific classes as: Closet, Chair and so on."""

    def __init__(self, name, weight):
        self._name = self.__verify_name(name)
        self._weight = self.__verify_weight(weight)

    @staticmethod
    def __verify_name(name):
        if not isinstance(name, str):
            raise TypeError('название должно быть строкой')
        return name

    @staticmethod
    def __verify_weight(value):
        if value <= 0:
            raise TypeError('вес должен быть положительным числом')
        return value


class Closet(Furniture):
    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._name = name
        self._weight = weight
        self._tp = tp
        self._doors = doors

    def get_attrs(self):
        return tuple(self.__dict__.keys())


class Chair(Furniture):
    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._name = name
        self._weight = weight
        self._height = height

    def get_attrs(self):
        return tuple(self.__dict__.keys())


class Table(Furniture):

    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._name = name
        self._weight = weight
        self._height = height
        self._square = square

    def get_attrs(self):
        return tuple(self.__dict__.values())
