from math import sqrt


class Descriptor:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        instance.__dict__[self.name] = value


class Triangle:
    """This class describes Triangle."""

    a = Descriptor()
    b = Descriptor()
    c = Descriptor()

    def __init__(self, a: (int, float), b: (int, float), c: (int, float)):
        if a < b + c and b < a + c and c < a + b:
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError("с указанными длинами нельзя образовать треугольник")

    def __len__(self):
        return self.a + self.b + self.c

    def __call__(self, *args, **kwargs):
        p = len(self) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
