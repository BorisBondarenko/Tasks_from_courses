class Ellipse:
    """This class describes the Ellipse as an object on the coordinate plane.
    Each attr will be created if it will be present, else not."""

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_coords(self):
        for i in ('x1', 'x2', 'y1', 'y2'):
            if not self.__dict__.get(i, False):
                raise AttributeError('нет координат для извлечения')
        return self.x1, self.y1, self.x2, self.y2

    def __setattr__(self, key, value):
        if value:
            self.__dict__[key] = value

    def __bool__(self):
        return len(self.__dict__.values()) == 4


lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(5, 6, 7, 8)]

for i in lst_geom:
    if i:
        i.get_coords()
