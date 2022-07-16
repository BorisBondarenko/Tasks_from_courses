class DeltaClock:
    """This class describes the objects that count the dif between two Clock-objects"""

    def __init__(self, clock_1, clock_2):
        self.clock_1 = clock_1
        self.clock_2 = clock_2

    def __len__(self):
        dif = self.clock_1.get_time() - self.clock_2.get_time()
        return dif if dif >= 0 else 0

    def __str__(self):
        dif = len(self)
        tmp = {'H': 3600, 'M': 60, 'S': 1}

        if dif < 0:
            return f'{0:02}: {0:02}: {0:02}'
        else:
            for name, amount in tmp.items():
                div = tmp[name]
                tmp[name] = dif // div
                dif %= div
            return f'{tmp["H"]:02}: {tmp["M"]:02}: {tmp["S"]:02}'


class Clock:
    """This class describes the Clock-objects"""

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds
