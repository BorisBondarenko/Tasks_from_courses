class StackObj:
    """This class describes the objects of linked-list in Stack-instance.
    attr: data - some str-date inside instance;
    attr: next - next new StackObj-obj;
    attr: prex old StackObj-obj"""

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Stack:
    """This class describes the Linked-List as an object.
    attr: top - first added element (StackObj - instance);
    attr: head - last added element;
    attr: __len - length of Linked-list."""

    def __init__(self):
        self.top = None
        self.head = None
        self.__len = 0

    def push(self, obj):
        if not self.top:
            self.top, self.head = obj, obj
            self.head.prev = self.top
        else:
            obj.prev = self.head
            self.head.next = obj
            self.head = obj
        self.__len += 1

    def pop(self):
        for_pop = self.head
        self.head = self.head.prev
        self.head.next = None
        self.__len -= 1
        return for_pop

    def __getitem__(self, idx):
        if idx > self.__len - 1:
            raise IndexError('неверный индекс')

        result = self.top
        while idx:
            result = result.next
            idx -= 1
        return result

    def __setitem__(self, idx, value):
        self[idx].data = value.data if isinstance(value, StackObj) else value
