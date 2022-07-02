class StringValue:
    """This descriptor validates product name by type and len of input value"""

    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name, None)

    def __set__(self, instance, string):
        if isinstance(string, str) and self.min_length <= len(string) <= self.max_length:
            setattr(instance, self.name, string)


class PriceValue:
    """This descriptor validates product price by type and price-range of input value"""
    def __init__(self, max_value):
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        if isinstance(value, int) and value <= self.max_value:
            setattr(instance, self.name, value)


class SuperShop:
    """This class describes the model of web-store"""
    def __init__(self, shop_name):
        self.shop_name = shop_name
        self.goods = []

    def add_product(self, product):
        """To add new product"""
        self.goods.append(product)

    def remove_product(self, product):
        """To remove some product"""
        self.goods.remove(product)


class Product:
    """This class describes the product using name and price"""

    name = StringValue(2, 50)
    price = PriceValue(10000)

    def __init__(self, name, price):
        self.name = name
        self.price = price
