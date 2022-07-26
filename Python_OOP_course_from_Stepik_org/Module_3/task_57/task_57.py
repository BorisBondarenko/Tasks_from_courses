class TableValues:
    """This class describes the table of same-type objects.
    attr: cells - matrix (table) of elements"""

    def __new__(cls, *args, **kwargs):
        if not kwargs.get('cell', None):
            raise ValueError('параметр cell не указан')
        return super().__new__(cls)

    def __init__(self, rows, cols, cell):
        self.cells = [[cell() for _ in range(cols)] for _ in range(rows)]

    def __getitem__(self, idx_s):
        return self.cells[idx_s[0]][idx_s[-1]].value

    def __setitem__(self, idx_s, value):
        self.cells[idx_s[0]][idx_s[-1]].value = value


class IntegerValue:
    """This class-descriptor for CellInteger-class attributes."""

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError('возможны только целочисленные значения')
        instance.__dict__[self.name] = value


class CellInteger:
    """This class describes the instances that will be used as cell in TableValues - objects.
    attr: value (descriptor-obj) with int value."""

    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value
