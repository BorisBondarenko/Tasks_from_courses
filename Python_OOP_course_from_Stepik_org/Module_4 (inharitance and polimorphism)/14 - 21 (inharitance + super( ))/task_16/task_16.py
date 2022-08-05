class SellItem:
    """This class describes reality objects in general (flats, houses, land).
    Further this class will used as basic-class for another smaller classes.
    attr: name - obj name;
    attr: price - price of object."""

    def __init__(self, name, price):
        self.name = name
        self.price = price


class House(SellItem):
    """This class describes House as reality object, his parent class - SellItem.
    attrs: name, price were inherited from basic class;
    attr: material - construction material;
    attr: square - total square of house."""

    def __init__(self, name, price, material, square):
        super().__init__(name, price)
        self.material = material
        self.square = square


class Flat(SellItem):
    """This class describes Flat as reality object, his parent class - SellItem.
        attrs: name, price were inherited from basic class;
        attr: size - total size;
        attr: rooms - total rooms."""

    def __init__(self, name, price, size, rooms):
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms


class Land(SellItem):
    """This class describes Land as reality object, his parent class - SellItem.
            attrs: name, price were inherited from basic class;
            attr: square - total square."""

    def __init__(self, name, price, square):
        super().__init__(name, price)
        self.square = square


class Agency:
    """Class Agency was created to manage all reality objects.
    attr: name - agency name;
    private attr: __objects - list of added objects for sale"""

    def __init__(self, name):
        self.name = name
        self.__objects = []

    def add_object(self, obj):
        if not isinstance(obj, SellItem):
            raise TypeError('Wrong data-type!')
        self.__objects.append(obj)

    def remove_object(self, obj):
        if obj in self.__objects:
            self.__objects.remove(obj)

    def get_objects(self):
        return self.__objects
