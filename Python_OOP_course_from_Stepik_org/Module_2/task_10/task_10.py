class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, new_next):
        if isinstance(new_next, StackObj | None):
            self.__next = new_next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, new_data):
        self.__data = new_data


class Stack:

    def __init__(self):
        self.top = None
        self.data_obj = []

    def push(self, obj):
        self.data_obj.append(obj)
        if self.top is None:
            self.top = obj

    def pop(self):
        self.data_obj.pop(-1)
        if len(self.data_obj) == 0:
            self.top = None

    def get_data(self):
        return list(map(lambda x: x.data, self.data_obj))