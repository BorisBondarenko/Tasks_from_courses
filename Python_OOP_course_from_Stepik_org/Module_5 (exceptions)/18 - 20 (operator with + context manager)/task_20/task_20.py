class Box:

    def __init__(self, name, max_weight):
        self._name = name
        self._max_weight = max_weight
        self._things = []

    def add_thing(self, obj):
        obj_name, obj_weight = obj
        if sum([i[-1] for i in self._things]) + obj_weight > self._max_weight:
            raise ValueError('превышен суммарный вес вещей')
        self._things.append(obj)

    def __getitem__(self, item):
        return self


class BoxDefender:

    def __init__(self, box):
        self.__box = box

    def __enter__(self):
        self.__tmp = Box(self.__box._name, self.__box._max_weight)
        return self.__tmp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__box._things.extend(self.__tmp._things)
        return False
