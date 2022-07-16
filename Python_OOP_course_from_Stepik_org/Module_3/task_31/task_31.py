class Budget:
    """This class describes the budget-instances."""

    def __init__(self):
        self.lst = []

    def add_item(self, it):
        if not isinstance(it, Item):
            raise TypeError('I\'m work with Item-objects')
        self.lst.append(it)

    def remove_item(self, indx):
        self.lst.pop(indx)

    def get_items(self):
        return self.lst


class Item:
    """This class describes the instances of spending-items."""

    def __init__(self, name, money: int | float):
        self.name = name
        self.money = money

    def __add__(self, other):
        money = self.money + other
        return Item(self.name, money).money

    def __radd__(self, other):
        return self + other