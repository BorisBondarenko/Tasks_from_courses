class Stack:
    """This class describes the stack of linked-list objects.
    attr: top - first added obj;
    attr: head - last added obj."""

    def __init__(self):
        self.top = StackObj('start_data')
        self.head = None

    def __len__(self):
        return sum((1 for _ in self))

    def __getitem__(self, idx):
        return self.loop(self.top, idx).data

    def __setitem__(self, idx, value):
        self.loop(self.top, idx).data = value

    def __iter__(self):
        obj = self.top
        while obj:
            yield obj
            obj = obj.next

    def __type_checker(self, obj):
        if not isinstance(obj, StackObj):
            raise TypeError("Я умею работать только с StackObj")
        return True

    def push_back(self, obj):
        self.__type_checker(obj)
        if self.head is None:
            self.top, self.head = obj, obj
        else:
            self.head.next = obj
        self.head = obj

    def push_front(self, obj):
        self.__type_checker(obj)
        obj.next, self.top = self.top, obj

    def loop(self, top, idx, counter=0):
        if idx > len(self) - 1:
            raise IndexError('неверный индекс')
        return top if idx == counter else self.loop(top.next, idx, counter + 1)


class StackObj:
    """This class describes the objects of elements that will be used in linked-list."""
    def __init__(self, data):
        self.data = data
        self.next = None