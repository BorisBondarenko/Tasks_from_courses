from random import sample


class Cell():
    def __init__(self, around_mines, mine):
        self.around_mines = around_mines  # кол-во мин вокруг
        self.mine = mine  # наличие мины в текущей клетке
        self.fl_open = False  # закрыли либо открыта клетка


class GamePole():

    def __init__(self, N, M):
        self.N = N  # размерность поля
        self.M = M  # число мин на поле

        rand = list(range(self.N ** 2))
        self.for_mining = sorted(sample(rand, M))
        self.pole = []

        for j in range(N):  # row
            row = []
            for i in range(j * 10, (j + 1) * 10):  # cell
                row.append(Cell(i + 1, True if i + 1 in self.for_mining else False))
            self.pole.append(row)

        for i in range(1, N + 1):  # row
            for j in range(1, N + 1):  # cell
                rows = self.pole[i - 2 if i - 1 else 0: i + 1]
                sector = sum(map(lambda x: x[j - 2 if j - 1 else 0: j + 1], rows), [])
                self.pole[i - 1][j - 1].around_mines = len(list(filter(lambda x: x.mine == True, sector)))

    def show(self):
        for i in self.pole:
            for j in i:
                print('*' if j.mine else j.around_mines, end=' ')
            print()

pole_game = GamePole(10, 12)
