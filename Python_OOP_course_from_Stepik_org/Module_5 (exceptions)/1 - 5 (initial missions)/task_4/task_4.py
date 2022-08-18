class Triangle:
    """This class describes triangle as an object."""

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        self.triangle_checker()

    def __setattr__(self, key, value):
        # before creating attr we should check the value
        if not isinstance(value, (int, float)) or value <= 0:
            raise TypeError('стороны треугольника должны быть положительными числами')
        self.__dict__[key] = value

    def triangle_checker(self):
        # checker using aspect ratio of triangle

        sights = list(self.__dict__.values())[:]

        for num in range(len(sights)):
            _ = sights.pop(num)
            if _ >= sum(sights):
                raise ValueError('из указанных длин сторон нельзя составить треугольник')
            sights.insert(num, _)


input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]

lst_tr = []
for i in input_data:
    # here I add new triangle into the res-list in case without errors
    try:
        lst_tr.append(Triangle(*i))
    except (ValueError, TypeError):
        pass

print(lst_tr)
