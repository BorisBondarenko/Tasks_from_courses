from math import sqrt


class PathLines:

    def __init__(self, *args):
        self.line_base = [LineTo(0, 0)]
        self.line_base.extend(args)

    def get_path(self):
        return self.line_base

    def get_length(self):
        lenght = 0
        for i in range(1, len(self.line_base)):
            x1 = self.line_base[i].x
            y1 = self.line_base[i].y
            x0 = self.line_base[i - 1].x
            y0 = self.line_base[i - 1].y

            lenght += sqrt(pow(x1 - x0, 2) + pow(y1 - y0, 2))

        return lenght

    def add_line(self, line):
        self.line_base.append(line)


class LineTo:

    def __init__(self, x, y):
        self.x = x
        self.y = y
