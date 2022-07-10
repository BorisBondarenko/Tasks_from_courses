class Integer:

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class LinkedList:
    OBJ_LIST = []

    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if isinstance(obj, ObjList):
            if self.OBJ_LIST:
                self.OBJ_LIST[-1].next = obj
                obj.prev = self.OBJ_LIST[-1]

                self.OBJ_LIST.append(obj)

                self.head = self.OBJ_LIST[0]
                self.tail = self.OBJ_LIST[-1]

            else:
                self.OBJ_LIST.append(obj)

    def remove_obj(self, indx):
        self.OBJ_LIST.pop(indx)

        for i, obj in enumerate(self.OBJ_LIST):
            obj.next = self.OBJ_LIST[i + 1] if i + 1 < len(self.OBJ_LIST) else None
            obj.prev = self.OBJ_LIST[i - 1] if i - 1 >= 0 else None

        self.head = self.OBJ_LIST[0]
        self.tail = self.OBJ_LIST[-1]

    def __len__(self):
        return len(self.OBJ_LIST)

    def __call__(self, idx, *args, **kwargs):
        return self.OBJ_LIST[idx].data


class ObjList:
    data = Integer()
    prev = Integer()
    next = Integer()

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


linked_lst = LinkedList()
obj = ObjList("Boris")
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
s = linked_lst(1)  # s = Balakirev
