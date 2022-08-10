class MoneyOperators:
    """This class describes arithmetic operation about Money-objects."""

    def __add__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money + other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money + other.money)

    def __sub__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money - other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money - other.money)


class Money:
    """This class describes Money as an object."""

    def __init__(self, value):
        self._money = self.check_val(value)

    @staticmethod
    def check_val(value):
        if not isinstance(value, (int, float)):
            raise TypeError('сумма должна быть числом')
        return value

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, new_value):
        self._money = self.check_val(new_value)


class MoneyR(Money, MoneyOperators):
    """This is the child class from Money and MoneyOperators class,
    and describes some wallet."""

    def __str__(self):
        return f"MoneyR: {self.money}"


class MoneyD(Money, MoneyOperators):
    """This is the child class from Money and MoneyOperators class,
        and describes some wallet."""

    def __str__(self):
        return f"MoneyD: {self.money}"
