class ShopInterface:
    """This is the parent class for ShopItems with abstract-meth get_id (id getter)."""

    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    __OBJ_ID = 0

    def __new__(cls, *args, **kwargs):
        cls.__OBJ_ID += 1
        return object.__new__(cls)

    def __init__(self, name, weight, price):
        self.__id = self.__OBJ_ID
        self._name = name
        self._weight = weight
        self._price = price

    def get_id(self):
        return self.__id
