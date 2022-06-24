class LinkedList:

    def __init__(self):
        self.__data = []
        self.head = None
        self.tail = None

    def add_obj(self, obj):

        obj.set_steck(self)
        obj.set_prev(self.__data[-1]) if self.__data else obj.set_prev(None)

        self.__data.append(obj)
        self.tail = obj

        if len(self.__data) >= 2:
            self.__data[-2].set_next(obj)

        if not self.head:
            self.head = obj

    def remove_obj(self):
        self.__data.pop(-1)

        if self.__data:
            self.__data[-1].set_next(None)
            self.tail = self.__data[-1]
        else:
            self.head = None

    def get_data(self):
        return list(map(lambda x: x.get_data(), self.__data))


class ObjList:

    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data
        self.steck_obj = None

    def set_steck(self, steck_obj: LinkedList):
        self.steck_obj = steck_obj

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def get_data(self):
        return self.__data


lst = LinkedList()
obj_1 = ObjList('данные 1')
obj_2 = ObjList('данные 2')
obj_3 = ObjList('данные 3')

lst.add_obj(obj_1)
lst.add_obj(obj_2)

print(obj_1.get_prev())
print(obj_1.get_next())

print()

print(obj_2.get_prev())
print(obj_2.get_next())

print()
