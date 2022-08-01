class Singleton:
    """This Singleton class will be used as parent-class for another child-class,
    that should exist in limited edition."""

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object().__new__(cls)
            return cls.__instance
        else:
            return cls.__instance


class Game(Singleton):
    """Child-class from Singleton class"""

    def __init__(self, name):
        old_name = getattr(self, 'name', False)
        self.name = old_name if old_name else name


g_1 = Game('boris')
g_2 = Game('igor')

print(g_1.name)
print(g_2.name)

print(id(g_1))
print(id(g_2))
