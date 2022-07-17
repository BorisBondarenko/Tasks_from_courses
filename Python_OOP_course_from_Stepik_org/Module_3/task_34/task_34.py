from math import sqrt


class Track:
    """This class describes the Track objects.
    start_x, start_y - x, y coords from where our objects will start the track;
    lines - the list of TrackLine - objects (pieses of track in general);
    length - the total length of whole track"""

    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.lines = []
        self.length = 0

    @staticmethod
    def __check_input(obj):
        if not isinstance(obj, Track):
            raise TypeError('Wrong data type, should be: TrackLine')
        return True

    def add_track(self, tr):
        if not isinstance(tr, TrackLine):
            raise TypeError('Wrong data type, should be: TrackLine')

        if not self.lines:
            self.length += sqrt(pow(tr.to_x - self.start_x, 2) + pow(tr.to_y - self.start_y, 2))
        elif self.lines:
            from_x, from_y = self.lines[-1].to_x, self.lines[-1].to_y
            self.length += sqrt(pow(tr.to_x - from_x, 2) + pow(tr.to_y - from_y, 2))

        self.lines.append(tr)

    def get_tracks(self):
        return tuple(self.lines)

    def __eq__(self, other):
        self.__check_input(other)
        return self.length == other.length

    def __lt__(self, other):
        self.__check_input(other)
        return self.length < other.length

    def __gt__(self, other):
        self.__check_input(other)
        return self.length > other.length

    def __len__(self):
        return int(self.length)


class TrackLine:

    """This class describes the TrackLine objects.
    This is object using to add to ours Track-objects"""

    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


track1, track2 = Track(0, 0), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2

print(res_eq)
