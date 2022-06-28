class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        if self.coord_checker(x):
            self.__x = x
        else:
            self.__x = 0
        if self.coord_checker(y):
            self.__y = y
        else:
            self.__y = 0

    def coord_checker(self, value):
        if value != 0:
            return -100 <= value <= 1024

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if self.coord_checker(x):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if self.coord_checker(y):
            self.__y = y

    @staticmethod
    def norm2(obj):
        return pow(obj.x, 2) + pow(obj.y, 2)