from math import sqrt


class Integer:

    @classmethod
    def checker(self, number):
        if isinstance(number, (int, float)):
            return True
        raise ValueError("Неверный тип данных.")

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.checker(value):
            instance.__dict__[self.name] = value


class Complex:
    real = Integer()
    img = Integer()

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __abs__(self):
        return sqrt(pow(self.real, 2) + pow(self.img, 2))


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)

print(c_abs)