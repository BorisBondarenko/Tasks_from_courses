class Cart():
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f'{i.name}: {i.price}' for i in self.goods]


class Table():
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV():
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Notebook():
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cup():
    def __init__(self, name, price):
        self.name = name
        self.price = price

cart = Cart()
cart.add(TV('tosiba', 1200))
cart.add(TV('panasonic', 1180))
cart.add(Table('wood_table', 199))
cart.add(Table('macbook pro', 1999))
cart.add(Table('hp', 300))
cart.add(Table('cup', 5))


print(cart.get_list())
