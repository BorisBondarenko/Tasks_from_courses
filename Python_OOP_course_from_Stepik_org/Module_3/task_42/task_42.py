class Rect:
    """This class describes the objects of Rectangles in coordinate plane.
    attr: x - x coord of top left edge;
    attr: y - y coord of top left edge;
    attr: width - width of rectangle;
    attr: height - height of rectangle;
    meth: __hash__ - to override the calculation hash-method"""

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __hash__(self):
        return hash((self.width, self.height))


r1 = Rect(10, 5, 100, 50)
r2 = Rect(-10, 4, 100, 50)

h1, h2 = hash(r1), hash(r2)  # h1 == h2
print(h1 == h2)
