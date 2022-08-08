class ItemAttrs:

    def __getitem__(self, idx):
        return list(self.__dict__.values())[idx]

    def __setitem__(self, idx, value):
        key = list(self.__dict__.keys())[idx]
        self.__dict__[key] = value


class Point(ItemAttrs):

    def __init__(self, x, y):
        self.x = x
        self.y = y
