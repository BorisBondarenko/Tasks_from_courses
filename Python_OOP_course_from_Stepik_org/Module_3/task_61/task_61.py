class Bag:
    """This class describes the bag for things.
    attr: max_weight - that bag could contain;
    attr: things - list of added thing inside;
    attr: total_weight - total weight of added thing inside bag."""

    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.things = []
        self.total_weight = 0

    def add_thing(self, thing):
        if self.total_weight + thing.weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')
        self.things.append(thing)
        self.total_weight += thing.weight

    def idx_checker(self, idx):
        if idx > len(self.things) - 1 or not isinstance(idx, int):
            raise IndexError('неверный индекс')
        return True

    def __getitem__(self, idx):
        self.idx_checker(idx)
        return self.things[idx]

    def __setitem__(self, idx, thing):
        self.idx_checker(idx)
        if self.total_weight - self.things[idx].weight + thing.weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')
        self.total_weight = self.total_weight - self.things[idx].weight + thing.weight
        self.things[idx] = thing

    def __delitem__(self, idx):
        self.idx_checker(idx)
        self.total_weight -= self.things[idx].weight
        del self.things[idx]


class Thing:
    """This class describes the thing as an object that will be added into the bag.
    attr: name - name of thing (Book, Pen, ...);
    attr: weight - weight of thing."""

    def __init__(self, name: str, weight: (int, float)):
        self.name = name
        self.weight = weight