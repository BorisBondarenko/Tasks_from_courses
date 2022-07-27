class TicTacToe:
    """This class describes the TicTacToe - game as an object.
    attr: pole - game field"""

    def __init__(self):
        self.pole = [[Cell() for _ in range(3)] for _ in range(3)]

    def clear(self):
        for row in self.pole:
            for elem in row:
                elem.value, elem.is_free = 0, False

    def __getitem__(self, idx):
        if type(idx[0]) == int and type(idx[-1]) == int:
            row, elem = idx
            return self.pole[row][elem].value

        elif type(idx[0]) == slice and type(idx[-1]) == int:
            colm = idx[-1]
            return tuple(map(lambda x: x.value, [row[colm] for row in self.pole]))

        elif type(idx[0]) == int and type(idx[-1]) == slice:
            row = idx[0]
            return tuple(map(lambda x: x.value, self.pole[row]))

    def __setitem__(self, idx, value):
        row, elem = idx
        if row > 2 or elem > 2:
            raise IndexError('неверный индекс клетки')
        if bool(self.pole[row][elem]):
            raise ValueError('клетка уже занята')
        self.pole[row][elem].value = value


class Cell:
    """This class describes the cell of game-field.
    attr: is_free - tell us is this field open or closed;
    attr: value - takes 3 type of values (0 - cell is vacant, 1 - cross; 2 - zero)"""

    def __init__(self):
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return self.is_free
