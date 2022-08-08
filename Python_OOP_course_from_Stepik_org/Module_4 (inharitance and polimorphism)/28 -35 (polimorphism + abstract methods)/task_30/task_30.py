class Validator:
    """This is the parent class for Validators with abstract-meth _is_valid."""

    def _is_valid(self, data):
        raise NotImplementedError('в классе не переопределен метод _is_valid')


class FloatValidator(Validator):

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value, *args, **kwargs):
        return self._is_valid(value)

    def _is_valid(self, data):
        if not isinstance(data, float):
            return False
        if data > self.max_value or data < self.min_value:
            return False
        return True
