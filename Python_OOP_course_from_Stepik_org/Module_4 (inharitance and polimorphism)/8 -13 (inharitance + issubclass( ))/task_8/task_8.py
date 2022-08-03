class ListInteger(list):
    """This subclass makes the validation fot input-value to list"""

    def value_checker(self, value):
        if not isinstance(value, int):
            raise TypeError('можно передавать только целочисленные значения')
        return value

    def __init__(self, args):
        lst = [self.value_checker(i) for i in args]
        super().__init__(lst)

    def __setitem__(self, key, value):
        value = self.value_checker(value)
        super().__setitem__(key, value)

    def append(self, value):
        value = self.value_checker(value)
        super().append(value)
