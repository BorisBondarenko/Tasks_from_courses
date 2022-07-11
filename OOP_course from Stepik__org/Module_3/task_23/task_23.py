from math import sqrt


class RadiusVector:
    """This class describes the radius-vectors as an objects"""

    def __init__(self, *args):
        if len(args) == 1:
            for num in range(1, args[0] + 1):
                self.__dict__[f'coord_{num}'] = 0
        elif len(args) > 1:
            for num, coord in enumerate(args, 1):
                self.__dict__[f'coord_{num}'] = coord

    def __len__(self):
        return len(self.__dict__)

    def __abs__(self):
        return sqrt(sum(map(lambda x: pow(x, 2), self.get_coords())))

    def set_coords(self, *args):
        for num, coord in enumerate(args, 1):
            if num > len(self.__dict__):
                break
            self.__dict__[f'coord_{num}'] = coord

    def get_coords(self):
        return tuple(self.__dict__.values())
