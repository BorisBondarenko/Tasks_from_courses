class Bag:
    """This class describe the model of back-pack"""

    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = []

    @property
    def things(self):
        """To return list of things in the bag"""
        return self.__things

    def add_thing(self, thing):
        """To add to list of things in the bag"""
        if isinstance(thing, Thing) and thing.weight + self.get_total_weight() <= self.max_weight:
            self.__things.append(thing)

    def remove_thing(self, indx):
        """To remove from list of things in the bag"""
        self.__things.pop(indx)

    def get_total_weight(self):
        """To get total weight of things in the bag"""
        if self.__things:
            return sum(i.weight for i in self.__things)
        else:
            return 0


class Thing:
    """This class describe the things that'll be added in the bag instance"""

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
