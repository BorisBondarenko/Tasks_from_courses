class Circle:
    """This class describes the circle"""

    def __init__(self, x, y, radius):
        """Operations of getting and setting making with using @property"""
        self.x = x
        self.y = y
        self.radius = radius

    def __setattr__(self, key, value):
        """Here we set the some-rules of validation"""
        if type(value) not in (int, float):
            raise TypeError("Incorrect value-type")
        if key == 'radius' and value < 1:
            return
        super().__setattr__(key, value)

    def __getattr__(self, item):
        return False

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new_x):
        self.__x = new_x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, new_y):
        self.__y = new_y

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, new_radius):
        self.__radius = new_radius