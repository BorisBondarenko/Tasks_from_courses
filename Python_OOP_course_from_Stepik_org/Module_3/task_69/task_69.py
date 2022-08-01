from random import choice


class TicTacToe:
    """This class describes the game TicTacToe.
    attr: pole - game field;
    attrs: __human_win, __computer_win, __draw - result flags that incites to over game."""

    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2
    PRINT_SYMBOLS = {0: '_', 1: 'X', 2: 'O'}

    def __init__(self):
        self.pole = [[Cell() for _ in range(3)] for _ in range(3)]
        self.__human_win = self.__computer_win = self.__draw = False

    @property
    def is_human_win(self):
        return self.__human_win

    @property
    def is_computer_win(self):
        return self.__computer_win

    @property
    def is_draw(self):
        return self.__draw

    def check_idx(self, pair):
        check_res = all(map(lambda x: type(x) == int and x in range(3), pair))
        if not check_res:
            raise IndexError('некорректно указанные индексы')
        return pair

    def is_finish(self):
        ran = list(range(3))
        pole = self.pole

        test_1 = [self[idx, idx] for idx in ran if self[idx, idx]]
        test_2 = [self[row, col] for row, col in zip(ran, ran[::-1]) if self[row, col]]

        test_3 = [[row[idx].value for row in pole if not row[idx]] for idx in ran]
        test_3 = list(*filter(lambda x: len(x) == 3, test_3))

        test_4 = [[el.value for el in row if not el] for row in pole]
        test_4 = list(*filter(lambda x: len(x) == 3, test_4))

        for test in (test_1, test_2, test_3, test_4):

            if test.count(self.HUMAN_X) == 3:
                self.__human_win = True
            elif test.count(self.COMPUTER_O) == 3:
                self.__computer_win = True
            elif not self.vacant_cells():
                self.__draw = True

    def vacant_cells(self):
        vacant_cells = [(r, c) for c in range(3) for r in range(3) if not self.pole[r][c].value]
        return vacant_cells

    def init(self):
        self.pole = [[Cell() for _ in range(3)] for _ in range(3)]
        self.__human_win = self.__computer_win = self.__draw = False

    def show(self):
        for row in self.pole:
            for cell in row:
                print(self.PRINT_SYMBOLS[cell.value], end='  ')
            print()

    def human_go(self):
        row, col = map(int, input('-> Your Turn: input coords (splited by space): ').split(' '))
        print('-' * 8)
        self[row, col] = self.HUMAN_X
        self.is_finish()

    def computer_go(self):
        print('-' * 8)
        row, col = choice(self.vacant_cells())
        self[row, col] = self.COMPUTER_O
        self.is_finish()

    def __getitem__(self, idx):
        row, col = self.check_idx(idx)
        return self.pole[row][col].value

    def __setitem__(self, idx, value):
        row, col = self.check_idx(idx)
        self.pole[row][col].value = value
        self.is_finish()

    def __bool__(self):
        return not any((self.is_human_win, self.is_computer_win, self.is_draw))


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return not bool(self.value)