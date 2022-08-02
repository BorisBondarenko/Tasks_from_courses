class Validator:
    """This class describes Validator-basic objects."""

    def _is_valid(self, data):
        return True

    def __call__(self, data, *args, **kwargs):
        if not self._is_valid(data):
            raise ValueError('данные не прошли валидацию')


class IntegerValidator(Validator):
    """This class inherit method __call__ from parent-class,
    and redefine method _is_valid (to validate just Int-data)."""

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        return isinstance(data, int) and self.min_value <= data <= self.max_value


class FloatValidator(Validator):
    """This class inherit method __call__ from parent-class,
        and redefine method _is_valid (to validate just Float-data)."""

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        return isinstance(data, int) and self.min_value <= data <= self.max_value


integer_validator = IntegerValidator(-10, 10)
float_validator = FloatValidator(-1, 1)
res1 = integer_validator(10)  # True
res2 = float_validator(10)  # исключение ValueError
