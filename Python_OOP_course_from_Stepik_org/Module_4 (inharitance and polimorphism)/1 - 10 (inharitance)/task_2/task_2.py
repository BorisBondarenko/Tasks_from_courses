class Thing:
    """This class describes the things inside some web-store.
    All attrs will be inherited by child-classes instances and then all of them will be processed.
    cls.attr: ID_COUNTER - used for create uniq id-number for each Thing."""

    ID_COUNTER = 1

    def __init__(self, name, price):
        self.id = Thing.ID_COUNTER
        self.name = name
        self.price = price
        self.memory = None
        self.frm = None
        self.weight = None
        self.dims = None
        Thing.ID_COUNTER += 1

    def get_data(self):
        return tuple(self.__dict__.values())


class Table(Thing):
    """This class comes as child-class of Thing - basic class,
    and describes the Table-objects in some web-store."""

    def __init__(self, name, price, weight, dims):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):
    """This class comes as child-class of Thing - basic class,
        and describes the eBook-objects in some web-store."""

    def __init__(self, name, price, memory, frm):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm
