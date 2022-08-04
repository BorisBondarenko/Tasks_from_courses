class Protists:
    """This is the Protists-class. This is class used as main-parent class for another."""
    def __init__(self, name, weight, old):
        self.name = name
        self.weight = weight
        self.old = old


class Plants(Protists):
    pass


class Animals(Protists):
    pass


class Mosses(Plants):
    pass


class Flowering(Plants):
    pass


class Worms(Animals):
    pass


class Mammals(Animals):
    pass


class Human(Mammals):
    pass


class Monkeys(Mammals):
    pass


class Monkey(Monkeys):
    pass


class Person(Human):
    pass


class Flower(Flowering):
    pass


class Worm(Worms):
    pass


classes = {Monkey: "мартышка, шимпанзе",
           Person: "Балакирев, Верховный жрец",
           Flower: "Тюльпан, Роза",
           Worm: "червь"}

data = (("мартышка", 30.4, 7),
        ("шимпанзе", 24.6, 8),
        ("Балакирев", 88, 34),
        ("Верховный жрец", 67.5, 45),
        ("Тюльпан", 0.2, 1),
        ("Роза", 0.1, 2),
        ("червь", 0.01, 1),
        ("червь 2", 0.02, 1))

lst_objs = []
for i in data:
    name = i[0].split(' ')[0]
    for cls, description in classes.items():
        if name in description:
            lst_objs.append(cls(*i))

lst_animals = [obj for obj in lst_objs if isinstance(obj, Animals)]
lst_plants = [obj for obj in lst_objs if isinstance(obj, Plants)]
lst_mammals = [obj for obj in lst_objs if isinstance(obj, Mammals)]
