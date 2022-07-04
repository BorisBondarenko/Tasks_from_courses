class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, new_a):
        self.__a = new_a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, new_b):
        self.__b = new_b

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, new_c):
        self.__c = new_c

    def __setattr__(self, key, value):
        if type(value) not in (int, float):
            return
        if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        if self.MIN_DIMENSION > value or value > self.MAX_DIMENSION:
            return
        super().__setattr__(key, value)
