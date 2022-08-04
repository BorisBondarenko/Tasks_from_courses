class IteratorAttrs:
    """This parent-class used as iterator for goods in some web-shop.
    By using it we can iterate every child-class object."""

    def __iter__(self):
        for k, v in self.__dict__.items():
            yield k, v


class SmartPhone(IteratorAttrs):
    """This class describes some smart-phone as an object with params:
    attr: model - phone model;
    attr: size - physical size of phone (tuple);
    attr: memory - RAM memory inside phone."""

    def __init__(self, model: str, size: tuple, memory: int):
        self.model = model
        self.size = size
        self.memory = memory
        super().__init__()


phone = SmartPhone('Iphone', (12, 6.5), 1024)

for attr in phone:
    print(attr)
