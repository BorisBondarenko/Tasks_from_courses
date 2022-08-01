class Animal:
    """This class describes animal as objects with name and age.
    This class made as parent-class for another child-classes that will be created further.
    attr: name - animal's name;
    attr: old - animal's age;
    meth: get_info - returns data about animal in string"""

    def __init__(self, name: str, old: int):
        self.name = name
        self.old = old

    def get_info(self):
        data = self.__dict__.values()
        return '{0}: {1}, {2}, {3}'.format(*data)


class Cat(Animal):
    """Class CAT describes cats.
        Attributes (name and old) were inherited from Animal (basic class).
        Method get_info also was inherited from Animal (parent class).
        attr: color - cat's color;
        attr: weight = cat's weight."""

    def __init__(self, name: str, old: int, color: str, weight: float):
        super().__init__(name, old)
        self.color = color
        self.weight = weight


class Dog(Animal):
    """Class DOG describes dogs.
        Attributes (name and old) were inherited from Animal (basic class).
        Method get_info also was inherited from Animal (parent class).
        attr: breed - dog's breed;
        attr: size = dog's size - tuple(height, length)."""

    def __init__(self, name: str, old: int, breed: str, size: tuple):
        super().__init__(name, old)
        self.breed = breed
        self.size = size
