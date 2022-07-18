class Dimensions:
    """This class describes the objects that are responsible for sizes of some ShopItem.
    MIN_DIMENSION - minimum allowable length for each size;
    MAX_DIMENSION - maximum allowable length for each size;
    __a, __b, __c - sizes"""

    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def get_all(self):
        return self.__a, self.__b, self.__c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, new_a):
        if self.MIN_DIMENSION <= new_a <= self.MAX_DIMENSION:
            self.__a = new_a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, new_b):
        if self.MIN_DIMENSION <= new_b <= self.MAX_DIMENSION:
            self.__b = new_b

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, new_c):
        if self.MIN_DIMENSION <= new_c <= self.MAX_DIMENSION:
            self.__c = new_c

    def __lt__(self, other):
        if isinstance(other, Dimensions):
            return self.get_all() < other.get_all()

    def __le__(self, other):
        if isinstance(other, Dimensions):
            return self.get_all() <= other.get_all()


class ShopItem:
    """This class describes the objects of some items in the some Shop.
    name - product name;
    price - product price;
    dim (dimensions) - Dimensions objects that are describe the sizes"""

    def __init__(self, name: str, price: (int, float), dim: Dimensions):
        self.name = name
        self.price = price
        self.dim = dim


lst_shop = [ShopItem('кеды', 1024, Dimensions(40, 30, 120)),
            ShopItem('зонт', 500.24, Dimensions(10, 20, 50)),
            ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)),
            ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))]

lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)
