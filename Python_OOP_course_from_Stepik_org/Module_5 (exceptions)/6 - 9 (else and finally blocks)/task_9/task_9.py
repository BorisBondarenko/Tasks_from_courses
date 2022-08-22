class Rect:

    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __setattr__(self, name, value):
        if name in ('_x', '_y'):
            if type(value) not in (int, float):
                raise ValueError('некорректные координаты и параметры прямоугольника')
        if name in ('_width', '_height'):
            if type(value) not in (int, float) or value <= 0:
                raise ValueError('некорректные координаты и параметры прямоугольника')
        self.__dict__[name] = value

    def __hash__(self):
        return hash((self._x, self._y, self._width, self._height))

    def __eq__(self, other):
        return hash(self) == hash(other)

    def is_collision(self, other):
        self_gor_range = set(range(self.x, self.x + self._width + 1))
        self_ver_range = set(range(self.y - self._height - 1, self.y))

        rect_gor_range = set(range(other.x, other.x + other._width + 1))
        rect_ver_range = set(range(other.y - other._height - 1, other.y))

        if self_ver_range & rect_ver_range and self_gor_range & rect_gor_range:
            raise TypeError('прямоугольники пересекаются')
        return True


coords = [(0, 0, 5, 3),
          (6, 0, 3, 5),
          (3, 2, 4, 4),
          (0, 8, 8, 1)]

lst_rect = [Rect(*i) for i in coords]

lst_not_collision = []

for rect in lst_rect:

    try:
        for elem in lst_rect:
            if rect != elem:
                rect.is_collision(elem)
    except TypeError:
        continue
    else:
        lst_not_collision.append(rect)

print(lst_not_collision)
