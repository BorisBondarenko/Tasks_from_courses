class Array:
    """This class describes the objects of same-type array.
    attr: max_length - max lenght array;
    attr: cell - link for class of value that will be used to add into array;
    attr: elements - list of array elements."""

    def __init__(self, max_length, cell):
        self.max_length = max_length
        self.cell = cell
        self.elements = [cell() for _ in range(max_length)]

    def __getitem__(self, idx):
        return self.elements[idx].value

    def __setitem__(self, idx, value):
        if idx < 0 or idx > self.max_length - 1:
            raise IndexError('неверный индекс для доступа к элементам массива')
        self.elements[idx].value = value

    def __delitem__(self, idx):
        del self.elements[idx]

    def __str__(self):
        return ' '.join([str(i.value) for i in self.elements])


class Integer:
    """This class describes the instances of int-values that will be added to our Array-objects.
    attr: __value - default value."""

    def __init__(self, start_value=0):
        self.__value = self.type_checker(start_value)

    @staticmethod
    def type_checker(value):
        if not isinstance(value, int):
            raise ValueError('должно быть целое число')
        return value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_val):
        self.__value = self.type_checker(new_val)
