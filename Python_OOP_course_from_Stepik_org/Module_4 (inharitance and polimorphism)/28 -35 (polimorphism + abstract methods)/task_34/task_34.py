class Track:
    """This class describes some track with points on the map.
    To create a track we should have some amount of points (objects class PointTrack).
    attr: _points - collection of points."""

    def __init__(self, *args):
        if len(args) == 2 and isinstance(args[0], (float, int)):
            self._points = [PointTrack(*args)]
        else:
            self._points = list(args)

    @property
    def points(self):
        return self._points

    def add_back(self, pt):
        if isinstance(pt, PointTrack):
            self._points.append(pt)

    def add_front(self, pt):
        if isinstance(pt, PointTrack):
            self._points.insert(0, pt)

    def pop_back(self):
        self._points.pop()

    def pop_front(self):
        self._points.pop(0)


class PointTrack:
    """This class describes the point of track on the map."""

    def __init__(self, x, y):
        self.x = self.check_coord(x)
        self.y = self.check_coord(y)

    @staticmethod
    def check_coord(value):
        if not isinstance(value, (int, float)):
            raise TypeError('координаты должны быть числами')
        return value

    def __str__(self):
        return f"PointTrack: {self.x}, {self.y}"
