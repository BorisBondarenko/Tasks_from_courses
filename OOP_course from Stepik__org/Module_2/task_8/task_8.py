class Car:

    MIN_LEN = 2
    MAX_LEN = 100

    def __init__(self):
        self.__model = None

    def checker(self, string):
        if isinstance(string, str):
            return self.MIN_LEN <= len(string) <= self.MAX_LEN
        else:
            return False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_model):
        if self.checker(new_model):
            self.__model = new_model