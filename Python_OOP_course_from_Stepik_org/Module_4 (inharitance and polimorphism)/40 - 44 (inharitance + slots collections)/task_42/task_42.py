class Star:
    __slots__ = ('_name', '_massa', '_temp')

    def __init__(self, name, massa, temp):
        self._name = name
        self._massa = massa
        self._temp = temp


class WhiteDwarf(Star):
    __slots__ = ('_type_star', '_radius')

    def __init__(self, name, massa, temp, type_star, radius):
        super().__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius


class YellowDwarf(Star):
    __slots__ = ('_type_star', '_radius')

    def __init__(self, name, massa, temp, type_star, radius):
        super().__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius


class RedGiant(Star):
    __slots__ = ('_type_star', '_radius')

    def __init__(self, name, massa, temp, type_star, radius):
        super().__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius


class Pulsar(Star):
    __slots__ = ('_type_star', '_radius')

    def __init__(self, name, massa, temp, type_star, radius):
        super().__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius


s_1 = RedGiant('Альдебаран', 5, 3600, 'красный гигант', 45)
s_2 = WhiteDwarf('Сириус А', 2.1, 9250, 'белый карлик', 2)
s_3 = WhiteDwarf('Сириус B', 1, 8200, 'белый карлик', 0.01)
s_4 = YellowDwarf('Солнце', 1, 6000, 'желтый карлик', 1)

stars = [s_4, s_3, s_2, s_1]
white_dwarfs = [i for i in stars if isinstance(i, WhiteDwarf)]
