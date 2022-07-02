class FloatValue:
    """This is the descriptor for Cell-class"""

    @classmethod
    def float_checker(cls, inp_val):
        """This is the checker for input values (if not float -> TypeError)"""
        if type(inp_val) != float:
            raise TypeError("You can use only FLOAT-values. Wake up!")
        return True

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if self.float_checker(value):
            instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class Cell:
    creation_counter = 0
    value = FloatValue()

    def __new__(cls, *args, **kwargs):
        """This func adds 1 to creation_counter value for every new instance"""
        cls.creation_counter += 1
        return super().__new__(cls)

    def __init__(self, inp_val):
        self.value = inp_val + self.creation_counter


class TableSheet:
    """This is the class that make two-dimension list and add to this our Cell-instances"""

    def __init__(self, n, m):
        self.cells = [[Cell(0.0) for j in range(n)] for i in range(m)]


table = TableSheet(3, 5)
