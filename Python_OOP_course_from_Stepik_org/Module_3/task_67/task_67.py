class TableValues:
    """This class describes the objects of Table.
    It means Table made of Cell's - objects.
    attr: rows - amount of rows in table;
    attr: cols - amount of cols in table;
    attr: type_data - type of data that used in table;
    attr: cells - table object."""

    def __init__(self, rows=0, cols=0, type_data=int):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.cells = [[Cell(0) for c in range(cols)] for r in range(rows)]

    def __getitem__(self, idx):
        row, col = idx
        return self.cells[row][col].data

    def __setitem__(self, idx, value):
        row, col = idx
        if not isinstance(value, self.type_data):
            raise TypeError('неверный тип присваиваемых данных')
        self.cells[row][col].data = value

    def __iter__(self):
        for i in self.cells:
            yield (cell.data for cell in i)


class Cell:
    """This class describes the Cell objects that will be used in Table.
    attr: __data - data the instance contain (insert due creating)."""

    def __init__(self, data):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, new_data):
        self.__data = new_data
