import time


class Mechanical:
    """This class describes the Mechanical water-filter."""

    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key not in self.__dict__.keys():
            if type(value) in (float, int) and value > 0:
                object.__setattr__(self, key, value)


class Aragon:
    """This class describes the Aragon water-filter."""

    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key not in self.__dict__.keys():
            if type(value) in (float, int) and value > 0:
                object.__setattr__(self, key, value)


class Calcium:
    """This class describes the Calcium water-filter."""

    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key not in self.__dict__.keys():
            if type(value) in (float, int) and value > 0:
                object.__setattr__(self, key, value)


class GeyserClassic:
    """This class describes the water-filter.

    It has 2 condition to be able to work.
    1. All filter-slots must be full (mechanical, aragon, calcium)
    2. And all from these filters must be 'fresh' to make their job"""

    MAX_DATE_FILTER = 100
    selection = {1: Mechanical, 2: Aragon, 3: Calcium}

    def __init__(self):
        self.slots = [None, None, None]

    def add_filter(self, slot_num, filter):
        if self.selection.get(slot_num) == type(filter) and self.slots[slot_num - 1] is None:
            self.slots[slot_num - 1] = filter

    def remove_filter(self, slot_num):
        self.slots[slot_num - 1] = None

    def get_filters(self):
        return self.slots

    def water_on(self):
        if None in self.slots:
            return False
        else:
            tmp = filter(lambda x: 0 < (time.time() - x.date) <= self.MAX_DATE_FILTER, self.slots)
            return True if len(list(tmp)) == 3 else False
