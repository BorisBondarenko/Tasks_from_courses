class Shop:

    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    id_x = 0

    def __init__(self, name='', weight=0, price=0):
        self.id = self.id_x
        self.name = name
        self.weight = weight
        self.price = price

    @classmethod
    def id_counter(cls):
        cls.id_x += 1

    def __setattr__(self, key, value):
        if key == 'name' and isinstance(value, str):
            self.id_counter()
            self.id = self.id_x
            return object.__setattr__(self, key, value)

        elif key == 'weight' and isinstance(value, int) and value > 0:
            return object.__setattr__(self, key, value)

        elif key == 'price' and isinstance(value, int) and value > 0:
            return object.__setattr__(self, key, value)

        elif key == 'id':
            pass

        else:
            raise TypeError("Неверный тип присваиваемых данных.")

        return object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
