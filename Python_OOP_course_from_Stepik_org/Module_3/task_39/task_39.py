# I solve it without inheritance (I know, this looks not so pretty as It could.)

class MoneyR:
    """This class describes objects MoneyR (RUB money account).
    __cb - link for CentralBank class."""

    def __init__(self, volume=0.0):
        self.__key = 'rub'
        self.__volume = volume
        self.__cb = None

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, new_cb):
        self.__cb = new_cb

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, new_volume):
        self.__volume = new_volume

    @property
    def key(self):
        return self.__key

    def __eq__(self, other):
        if not self.__cb or not other.cb:
            raise ValueError("Неизвестен курс валют.")
        a, b = self.__cb.cur_values(self, other)
        return a == b

    def __lt__(self, other):
        if not self.__cb or not other.cb:
            raise ValueError("Неизвестен курс валют.")
        a, b = self.__cb.cur_values(self, other)
        return a < b

    def __le__(self, other):
        if not self.__cb or not other.cb:
            raise ValueError("Неизвестен курс валют.")
        a, b = self.__cb.cur_values(self, other)
        return a <= b


class MoneyD:
    """This class describes objects MoneyD (DOLLAR money account).
        __cb - link for CentralBank class."""

    def __init__(self, volume=0.0):
        self.__key = 'dollar'
        self.__volume = volume
        self.__cb = None

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, new_cb):
        self.__cb = new_cb

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, new_volume):
        self.__volume = new_volume

    @property
    def key(self):
        return self.__key

    def __eq__(self, other):
        if not self.__cb or not other.cb:
            raise ValueError("Неизвестен курс валют.")
        a, b = self.__cb.cur_values(self, other)
        return a == b

    def __lt__(self, other):
        if not self.__cb or not other.cb:
            raise ValueError("Неизвестен курс валют.")
        a, b = self.__cb.cur_values(self, other)
        return a < b

    def __le__(self, other):
        if not self.__cb or not other.cb:
            raise ValueError("Неизвестен курс валют.")
        a, b = self.__cb.cur_values(self, other)
        return a <= b


class MoneyE:
    """This class describes objects MoneyE (EURO money account).
        __cb - link for CentralBank class."""

    def __init__(self, volume=0.0):
        self.__key = 'euro'
        self.__volume = volume
        self.__cb = None

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, new_cb):
        self.__cb = new_cb

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, new_volume):
        self.__volume = new_volume

    @property
    def key(self):
        return self.__key

    def __eq__(self, other):
        if not self.__cb or not other.cb:
            raise ValueError("Неизвестен курс валют.")
        a, b = self.__cb.cur_values(self, other)
        return a == b

    def __lt__(self, other):
        if not self.__cb or not other.cb:
            raise ValueError("Неизвестен курс валют.")
        a, b = self.__cb.cur_values(self, other)
        return a < b

    def __le__(self, other):
        if not self.__cb or not other.cb:
            raise ValueError("Неизвестен курс валют.")
        a, b = self.__cb.cur_values(self, other)
        return a <= b


class CentralBank:
    """This class describes Central Bank.
    We don't have any opportunity to create any instance of this class.
    Just use his inner functionality:

    attr: rates - currency rate
    meth: cur_values - convert the couple of currencies to dollar and return tuple.
    meth: register - this method input link for him self into register account.
    """

    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None

    @staticmethod
    def cur_values(a, b):
        a_currency = a.cb.rates[a.key]
        a_value = round(a.volume / a_currency, 2)
        b_currency = a.cb.rates[b.key]
        b_value = round(b.volume / b_currency, 2)
        return a_value, b_value

    @classmethod
    def register(cls, money):
        money.cb = cls
