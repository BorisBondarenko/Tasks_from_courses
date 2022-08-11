class Note:

    def __init__(self, name, ton=0):
        self._name = name
        self._ton = ton

    def __setattr__(self, attr, value):
        if attr == '_name' and value not in ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'):
            raise ValueError('недопустимое значение аргумента')
        elif attr == '_ton' and value not in (-1, 0, 1):
            raise ValueError('недопустимое значение аргумента')
        object.__setattr__(self, attr, value)


class Notes:
    __slots__ = ('_do', '_re', '_mi', '_fa', '_solt', '_la', '_si',)
    __notes = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        for name, note in zip(self.__slots__, self.__notes):
            object.__setattr__(self, name, Note(note))

    def __getitem__(self, idx):
        if idx not in range(0, 7):
            raise IndexError('недопустимый индекс')
        return self.__getattribute__(self.__slots__[idx])

    def __setitem__(self, idx, value):
        if idx not in range(0, 7):
            raise IndexError('недопустимый индекс')
        self.__setattr__(self.__slots__[idx], value)


notes = Notes()
