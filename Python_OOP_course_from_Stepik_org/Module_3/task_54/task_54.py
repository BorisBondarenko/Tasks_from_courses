class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.vals = tuple(self.__dict__.keys())

    def checker(self, idx):
        if not isinstance(idx, int) or idx > len(self.vals) - 1:
            raise IndexError('неверный индекс поля')
        return True

    def __getitem__(self, item):
        self.checker(item)
        return getattr(self, self.vals[item])

    def __setitem__(self, key, value):
        self.checker(key)
        setattr(self, self.vals[key], value)

    def __delitem__(self, key):
        self.checker(key)
        delattr(self, self.vals[key])
