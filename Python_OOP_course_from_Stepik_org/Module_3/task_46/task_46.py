class Descriptor:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        instance.__dict__[self.name] = value


class Dimensions:
    """This class describes the physical objects.
    attr: a - width;
    attr: b - height;
    attr: c - depth."""

    a = Descriptor()
    b = Descriptor()
    c = Descriptor()

    def __init__(self, a: (int, float), b: (int, float), c: (int, float)):
        self.a = a
        self.b = b
        self.c = c

    def __hash__(self):
        return hash((self.a, self.b, self.c))


s_inp = input()

lst_dims = []
for i in s_inp.split(';'):
    a, b, c = list(map(float, i.strip().split(' ')))
    lst_dims.append(Dimensions(a, b, c))

lst_dims = sorted(lst_dims, key=hash)
