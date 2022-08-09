class Digit:
    def __init__(self, value):
        if not isinstance(value, int):
            raise TypeError('значение не соответствует типу объекта')
        self.value = value


class Integer(Digit):
    def __init__(self, value):
        if not isinstance(value, int):
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class Float(Digit):
    def __init__(self, value):
        if not isinstance(value, float):
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class Positive(Digit):
    def __init__(self, value):
        if value <= 0:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class Negative(Digit):
    def __init__(self, value):
        if value >= 0:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class PrimeNumber(Integer, Positive):
    pass


class FloatPositive(Float, Positive):
    pass


digits = [PrimeNumber(5), PrimeNumber(1), PrimeNumber(100),
          FloatPositive(10.8), FloatPositive(0.3), FloatPositive(78.5),
          FloatPositive(5.5), FloatPositive(9.9)]

lst_positive = [i for i in digits if isinstance(i, Positive)]
lst_float = [i for i in digits if isinstance(i, Float)]
