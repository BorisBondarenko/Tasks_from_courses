class Track:
    """This class describes the objects of Tracks as sequence of dots on coordinate plane.
    attrs: start_x, start_y - start position (x, y) coords;
    attr: points - added points by using method 'add_point'."""

    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.points = {}

    def add_point(self, x, y, speed):
        self.points[(x, y)] = speed

    def idx_checker(self, idx):
        if idx > len(self.points):
            raise IndexError('некорректный индекс')

    def __getitem__(self, idx):
        key = list(self.points.keys())[idx]
        return key, self.points[key]

    def __setitem__(self, idx, value):
        key = list(self.points.keys())[idx]
        self.points[key] = value

    def __delitem__(self, idx):
        key = list(self.points.keys())[idx]
        del self.points[key]
