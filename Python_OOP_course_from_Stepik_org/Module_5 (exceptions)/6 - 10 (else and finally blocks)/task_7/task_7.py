class Point:
    """This class describes the point on the coordinate plane
    with coors (x, y)."""

    def __init__(self, x=0, y=0):
        self._x = x if x else 0
        self._y = y if y else 0

    def __str__(self):
        return f'Point: x = {self._x}, y = {self._y}'

    def __repr__(self):
        return f'Point: x = {self._x}, y = {self._y}'


a, b = input().split()
# Here I check the input-values (on is digit type) and create the Point-instances.
# In a positive case - I create Point-instance with the received values,
# else: Point-instance with zero-coords

try:
    a, b = int(a), int(b)
    res = Point(a, b)
except ValueError:
    try:
        a, b = float(a), float(b)
        res = Point(a, b)
    except ValueError:
        res = Point()
finally:
    print(res)
