from random import choice, randrange


class Line():
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect():
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse():
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


elements = []
class_list = [Line, Rect, Ellipse]

for i in range(217):
    coords = (randrange(-100, 100) for j in range(4))
    elements.append(choice(class_list)(*coords))

for elem in elements:
    if 'Line' in str(elem):
        elem.sp = (0, 0)
        elem.ep = (0, 0)