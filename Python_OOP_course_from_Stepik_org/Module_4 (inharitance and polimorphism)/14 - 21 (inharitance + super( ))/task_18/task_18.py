def integer_params_decorated(func):
    """This func is decorator for method inside class Vector."""

    def wrapper(*args):
        """Here I validate input values in every each method."""
        for i in args[1:]:
            if not isinstance(i, int):
                raise TypeError("аргументы должны быть целыми числами")
        result = func(*args)
        return result

    return wrapper


def integer_params(cls):
    """In this decorator I make logic that give me class method as func
    - than could be decorated (validation decorator)."""

    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))
    return cls


@integer_params
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    def set_coords(self, *coords, reverse=False):
        c = list(coords)
        self.__coords = c if not reverse else c[::-1]


vector = Vector(1, 2)
vector[1] = 20.4  # TypeError
