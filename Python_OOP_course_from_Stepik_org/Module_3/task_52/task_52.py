from random import sample


class Cell:

    def __init__(self):
        self.__number = 0
        self.__is_mine = False
        self.__is_open = True

    def __bool__(self):
        return not self.is_open

    @staticmethod
    def checker(value):
        if not isinstance(value, (int, bool)) or value not in range(9):
            raise ValueError("недопустимое значение атрибута")
        return True

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, new_val):
        self.checker(new_val)
        self.__is_mine = new_val

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, new_val):
        self.checker(new_val)
        self.__number = new_val

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, new_val):
        self.checker(new_val)
        self.__is_open = new_val


class GamePole:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, N, M, total_mines):
        self.N = N  # кол-во строк
        self.M = M  # кол-во столбцов
        self.total_mines = total_mines  # число мин на поле
        self.__pole_cells = []

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):

        rand = list(range(self.N * self.M))
        for_mining = sorted(sample(rand, self.total_mines))

        for j in range(self.N):
            row = []
            for i in range(self.M):
                pos = (j * self.M) + (i + 1)
                row.append(Cell())
                row[-1].is_mine = True if pos in for_mining else False

            self.pole.append(row)

        for i in range(1, self.N + 1):
            for j in range(1, self.M + 1):
                rows = self.pole[i - 2 if i - 1 else 0: i + 1]
                sector = sum(map(lambda x: x[j - 2 if j - 1 else 0: j + 1], rows), [])

                self.pole[i - 1][j - 1].number = len(list(filter(lambda x: x.is_mine, sector)))
                self.pole[i - 1][j - 1].is_open = False

    def show_pole(self):
        for i in self.pole:
            for j in i:
                print('*' if j.is_mine else j.number, end=' ')
            print()

    def open_cell(self, i, j):
        if i > self.N or i < 0:
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        if j > self.M or j < 0:
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        self.pole[i][j].is_open = True
