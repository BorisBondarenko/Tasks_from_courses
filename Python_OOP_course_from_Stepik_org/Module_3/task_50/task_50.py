from math import sqrt


class Line:
    """This class describes the line on the coordinate plane.
    attrs: x1, y1, x2, y2 - coordinates on plane."""

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __len__(self):
        return sqrt(pow(self.y2 - self.y1, 2) + pow(self.x2 - self.x1, 2)) >= 1
