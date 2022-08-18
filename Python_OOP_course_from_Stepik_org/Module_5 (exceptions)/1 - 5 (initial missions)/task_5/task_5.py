class FloatValidator:
    """The instances of this class makes validation of value by using allowable range
    and type of value (Float - only available).
    attr: min_value - low value of range;
    attr: min_value - top value of range."""

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value, *args, **kwargs):
        if type(value) != float or value > self.max_value or value < self.min_value:
            raise ValueError('значение не прошло валидацию')
        return value


class IntegerValidator:
    """The instances of this class makes validation of value by using allowable range
        and type of value (nt - only available).
        attr: min_value - low value of range;
        attr: min_value - top value of range."""

    def __init__(self, min_value, max_value):
        self.rng = range(min_value, max_value + 1)

    def __call__(self, value, *args, **kwargs):
        if type(value) != int or value not in self.rng:
            raise ValueError('значение не прошло валидацию')
        return value


def is_valid(lst, validators):
    res = []
    for i in lst:
        for validator in validators:
            try:
                res.append(validator(i))
            except ValueError:
                pass
    return res


# tests:
fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)

lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])
print(lst_out)
