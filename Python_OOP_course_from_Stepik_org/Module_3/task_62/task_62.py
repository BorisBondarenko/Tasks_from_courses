class SparseTable:
    """This class describes the big sparse table which has cells as an Cells - objects.
    attr: rows - total amount of rows in table;
    attr: cols - total amount of cols in table;
    attr: cells - cells holder made as dict (key: tuple(row, col), value: Cell(data))"""

    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.cells = {}

    def __refresher(self):
        self.rows = max(self.cells.keys(), key=lambda x: x[0])[0] + 1
        self.cols = max(self.cells.keys(), key=lambda x: x[-1])[-1] + 1

    def add_data(self, row, col, data):
        if (row, col) in self.cells.keys():
            raise IndexError('ячейка уже занята')
        self.cells[row, col] = data
        self.__refresher()

    def remove_data(self, row, col):
        if (row, col) not in self.cells.keys():
            raise IndexError('ячейка с указанными индексами не существует')
        del self.cells[(row, col)]
        self.__refresher()

    def __getitem__(self, idx):
        if idx not in self.cells.keys():
            raise ValueError('данные по указанным индексам отсутствуют')
        return self.cells[idx].value

    def __setitem__(self, idx, value):
        if idx not in self.cells.keys():
            self.cells[idx] = Cell(value)
            self.__refresher()
        elif idx in self.cells.keys():
            self.cells[idx].value = value


class Cell:
    """This class describes the cell-object that will be used in SparseTable-instance.
    attr: value - cell's value"""

    def __init__(self, value):
        self.value = value
