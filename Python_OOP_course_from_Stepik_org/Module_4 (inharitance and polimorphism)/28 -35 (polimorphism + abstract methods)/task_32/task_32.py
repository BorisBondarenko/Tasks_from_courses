from abc import ABC, abstractmethod


class StackInterface(ABC):
    """This class is basic-class for Stack-obj.
    His function is supply interface for child-classes."""

    @abstractmethod
    def push_back(self, obj):  # adding an element to the end of stack
        pass

    @abstractmethod
    def pop_back(self):  # removing an element from the end of stack
        pass


class Stack(StackInterface):
    """This is the main class here.
    His function is to manage the elements of linked-list (StackObj - instances)."""

    def __init__(self):
        self._top = None
        self._last = None

    def push_back(self, obj):
        if not isinstance(obj, StackObj):
            raise TypeError('You\'re not my type')

        if self._top is None and self._last is None:
            self._top = self._last = obj
        else:
            self._last._next = obj
            obj._prev = self._last
            self._last = obj

    def pop_back(self):
        res = self._last
        self._last = self._last._prev if self._last._prev else None
        if self._last:
            self._last._next = None
        else:
            self._top = None
        return res


class StackObj:
    """This class describes the elements of linked-list inside Stack."""

    def __init__(self, data):
        self._data = data
        self._next = None
        self._prev = None