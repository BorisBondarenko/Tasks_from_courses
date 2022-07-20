import sys


class ShopItem:
    """This class describes some Shop Items:
    attr: name - name of item;
    attr: weight - weight of item;
    attr: price - price of item."""


    def __init__(self, name: str, weight: (int, float), price: (int, float)):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)


def split_string(text):
    lst_words = text.strip().replace(':', '').split(' ')
    name = ' '.join(filter(lambda x: x.isalpha(), lst_words))
    weight, price = list(filter(lambda x: x.isdigit() or '.' in x, lst_words))
    return name, float(weight), float(price)


lst_in = list(map(lambda x: ShopItem(*split_string(x)), sys.stdin.readlines()))
shop_items = {k: [k, lst_in.count(k)] for k in lst_in}
