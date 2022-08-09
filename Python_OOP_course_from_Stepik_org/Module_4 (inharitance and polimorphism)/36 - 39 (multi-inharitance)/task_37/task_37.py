class ShopItem:
    """This class describes the shop-item in some book web-store.
    attr: _id is unique for every shop item inside web-store.
    And also this class using as parent for Book - instances."""

    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


class ShopGenericView:

    def __str__(self):
        res = [f'{name}: {val}' for name, val in self.__dict__.items()]
        return '\n'.join(res)


class ShopUserView:

    def __str__(self):
        res = [f'{name}: {val}' for name, val in self.__dict__.items() if name != '_id']
        return '\n'.join(res)


class Book(ShopItem, ShopUserView):
    """This is the Book class that describes books inside web-store.
    This is child-class from ShopItem.
    This class als inherit some functions of view info about self
    from two class (ShopUserView, ShopGenericView) by user's choice."""

    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


book = Book('The Fountainhead', 'Ayn Rand', 1943)
print(book)
