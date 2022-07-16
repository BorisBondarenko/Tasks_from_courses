class Descriptor:
    """This descriptor creates the setters and getters for StackObj attributes."""

    def __set_name__(self, owner, name):
        self.name = f"_{owner.__name__}__{name}"

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Stack:
    """This class describes the main object in this program.
    Stack-instance is created with a purpose to manage the StackObj-instances.
    For final the instance of this class it is the linked list-object"""

    def __init__(self):
        self.top = None

    def push_back(self, obj):
        if not self.top:
            self.top = obj
        elif self.top:
            next_obj = self.top
            while next_obj:
                if next_obj.next is None:
                    next_obj.next = obj
                    break
                next_obj = next_obj.next

    def pop_back(self):
        next_obj = self.top
        while next_obj:
            if next_obj.next:
                if next_obj.next.next is None:
                    next_obj.next = None
                    break
                else:
                    next_obj = next_obj.next
            else:
                break

    def __add__(self, other):
        self.push_back(other)
        return self

    def __iadd__(self, other):
        return self + other

    def __mul__(self, other):
        for data in other:
            self.push_back(StackObj(data))
        return self

    def __imul__(self, other):
        return self * other


class StackObj:
    """This class describes the objects-StackObj.
    StackObj-objects this is the simple instances
    that always will connect by link (attribute "next")
    with next object of this class that would be created."""

    data = Descriptor()
    next = Descriptor()

    def __init__(self, data):
        self.data = data
        self.next = None
