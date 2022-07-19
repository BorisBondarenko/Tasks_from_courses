class Box:
    """This class describes the Box as an object for common Things in our life.
    attr: things - for holding all of added things in one place;
    meth: add_things, get_things - methods to manage the box;
    meth: __eq__ - give the opportunity to compare the couple of Boxes."""

    def __init__(self):
        self.things = []

    def add_thing(self, obj):
        if isinstance(obj, Thing):
            self.things.append(obj)

    def get_things(self):
        return self.things

    def __eq__(self, other):
        a = sorted(map(lambda x: (x.name, x.mass), self.things))
        b = sorted(map(lambda x: (x.name, x.mass), other.get_things()))
        return a == b


class Thing:
    """This class describes the Thing as an object that add to Boxes.
    meth: __eq__- for comparison between the couple of Thing-objects"""

    def __init__(self, name: str, mass: (int, float)):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        if isinstance(other, Thing):
            a = self.name.lower(), self.mass
            b = other.name.lower(), other.mass
            return a == b


b1 = Box()
b2 = Box()

b1.add_thing(Thing('bread', 100))
b1.add_thing(Thing('spoon', 200))
b1.add_thing(Thing('nutella', 2000))

b2.add_thing(Thing('spoon', 200))
b2.add_thing(Thing('bread', 100))
b2.add_thing(Thing('nutella', 2000))

res = b1 == b2  # True
