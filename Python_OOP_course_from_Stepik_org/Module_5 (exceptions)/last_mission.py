from random import randint


class Ship:

    def __init__(self, length=0, tp=1, x=None, y=None):
        self._x = x
        self._y = y
        self._tp = tp
        self._length = length
        self._is_move = True
        self._cells = [1] * length
        self._perimeter = {}
        self._ship_cords = None

        if None not in (x, y):
            self.set_start_coords(x, y)

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y
        self._perimeter.clear()

        a, b = [self._length, 1] if self._tp == 1 else [1, self._length]
        coord_x, coord_y = list(range(x, x + a)), list(range(y, y + b))

        self._ship_cords = [(j, i) for j in coord_x for i in coord_y]
        self._perimeter = dict(zip(self._ship_cords, self._cells))

    def radius(self):
        x = self._x
        y = self._y

        a, b = [self._length + 1, 2] if self._tp == 1 else [2, self._length + 1]
        coord_x, coord_y = list(range(x - 1, x + a)), list(range(y - 1, y + b))
        return set((j, i) for j in coord_x for i in coord_y)

    def get_start_coords(self):
        return self._x, self._y

    def move(self, go):
        x = self._x + go if self._tp == 1 else self._x
        y = self._y + go if self._tp == 2 else self._y
        self.set_start_coords(x, y)

    def is_collide(self, other):
        a = self.radius()
        b = set(other._perimeter.keys())
        return bool(a & b)

    def is_out_pole(self, size=10):
        allowed_rng = range(0, size - 1)
        head = self._x if self._tp == 1 else self._y
        tail = head + self._length
        return False if head in allowed_rng and tail in allowed_rng else True

    def __getitem__(self, idx):
        return list(self._cells)[idx]

    def __setitem__(self, idx, value):
        self._cells[idx] = value
        self._is_move = False


class GamePole:

    def __init__(self, size=10):
        self._size = size
        self._ships = []
        self.pole = {}
        self.prepare_ships()

    def prepare_ships(self):
        for ship_amount, ship_size in enumerate(range(4, 0, -1), 1):
            for i in range(ship_amount):
                permission = False

                while not permission:
                    tp = randint(1, 2)
                    coord_x, coord_y = randint(0, self._size - 1), randint(0, self._size - 1)

                    ship = Ship(ship_size, tp, coord_x, coord_y)
                    if not ship.is_out_pole(self._size):

                        if self.is_vacant(ship):
                            self._ships.append(ship)
                            permission = True

    def init(self):
        self.pole = {(col, row): 0 for col in range(self._size) for row in range(self._size)}
        for ship in self._ships:
            self.pole.update(ship._perimeter)

    def is_vacant(self, ship):
        not_vacant_cords = set()

        for sh in self._ships:
            for cord in sh._ship_cords:
                not_vacant_cords.add(cord)

        inter_section = ship.radius() & not_vacant_cords
        return True if not inter_section else False

    def get_ships(self):
        return self._ships

    def ship_checker(self, ship):
        if not self.is_vacant(ship) or ship.is_out_pole():
            return False
        return True

    def move_ships(self):

        for s in self._ships:
            if not s._is_move:
                continue

            idx = self._ships.index(s)
            ship = self._ships.pop(idx)

            for step in (-1, 1, 0):
                ship.move(step)
                if self.ship_checker(ship):
                    self._ships.insert(idx, ship)
                    self.init()
                    break

    def show(self):
        for row in range(self._size):
            for col in range(self._size):
                print(self.pole[col, row], end='  ')
            print()

    def get_pole(self):
        res = [tuple(self.pole[col, row] for col in range(self._size)) for row in range(self._size)]
        return tuple(res)


# tests:

ship = Ship(2)
ship = Ship(2, 1)
ship = Ship(3, 2, 0, 0)
assert ship._length == 3 and ship._tp == 2 and ship._x == 0 and ship._y == 0, "неверные значения атрибутов объекта класса Ship"
assert ship._cells == [1, 1, 1], "неверный список _cells"
assert ship._is_move, "неверное значение атрибута _is_move"
ship.set_start_coords(1, 2)
assert ship._x == 1 and ship._y == 2, "неверно отработал метод set_start_coords()"
assert ship.get_start_coords() == (1, 2), "неверно отработал метод get_start_coords()"
ship.move(1)
s1 = Ship(4, 1, 0, 0)
s2 = Ship(3, 2, 0, 0)
s3 = Ship(3, 2, 0, 2)
assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 0)"
assert s1.is_collide(
    s3) == False, "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 2)"
s2 = Ship(3, 2, 1, 1)
assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 1, 1)"
s2 = Ship(3, 1, 8, 1)
assert s2.is_out_pole(10), "неверно работает метод is_out_pole() для корабля Ship(3, 1, 8, 1)"
s2 = Ship(3, 2, 1, 5)
assert s2.is_out_pole(10) == False, "неверно работает метод is_out_pole(10) для корабля Ship(3, 2, 1, 5)"
s2[0] = 2
assert s2[0] == 2, "неверно работает обращение ship[indx]"
p = GamePole(10)
p.init()
for nn in range(5):
    for s in p._ships:
        assert s.is_out_pole(10) == False, "корабли выходят за пределы игрового поля"
        for ship in p.get_ships():
            if s != ship:
                assert s.is_collide(ship) == False, "корабли на игровом поле соприкасаются"
    p.move_ships()

gp = p.get_pole()
assert type(gp) == tuple and type(gp[0]) == tuple, "метод get_pole должен возвращать двумерный кортеж"
assert len(gp) == 10 and len(gp[0]) == 10, "неверные размеры игрового поля, которое вернул метод get_pole"
pole_size_8 = GamePole(8)
pole_size_8.init()
