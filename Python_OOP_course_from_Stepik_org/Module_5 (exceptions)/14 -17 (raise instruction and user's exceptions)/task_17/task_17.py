class CellException(Exception):
    pass


class CellIntegerException(CellException):
    pass


class CellFloatException(CellException):
    pass


class CellStringException(CellException):
    pass


class CellInteger:

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_val):
        if self.min_value > new_val or new_val > self.max_value:
            raise CellIntegerException('значение выходит за допустимый диапазон')
        self._value = new_val


class CellFloat:

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_val):
        if self.min_value > new_val or new_val > self.max_value:
            raise CellFloatException('значение выходит за допустимый диапазон')
        self._value = new_val


class CellString:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_val):
        if self.min_length > len(new_val) or len(new_val) > self.max_length:
            raise CellStringException('длина строки выходит за допустимый диапазон')
        self._value = new_val


class TupleData:

    def __init__(self, *args):
        self.data = list(args)

    def __setattr__(self, key, value):
        val = [i for i in value if isinstance(i, (CellInteger, CellFloat, CellString))]
        self.__dict__[key] = val

    def __setitem__(self, idx, value):
        if idx > len(self.data):
            raise IndexError
        self.data[idx].value = value

    def __getitem__(self, idx):
        if idx > len(self.data):
            raise IndexError
        return self.data[idx]

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return (i.value for i in self.data)


ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")
