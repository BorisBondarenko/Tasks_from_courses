class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, x1, y1, x2=0, y2=0):
        self.__sp = self.__ep = None

        if isinstance(x1, int) and isinstance(y1, int):
            self.__sp = Point(x1, y1)
            self.__ep = Point(x2, y2)

        elif isinstance(x1, Point) and isinstance(y1, Point):
            self.__sp = x1
            self.__ep = y1

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(f'Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords()}')


rect = Rectangle(Point(0, 0), Point(20, 34))