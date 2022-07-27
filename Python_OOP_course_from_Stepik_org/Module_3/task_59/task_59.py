class RadiusVector:
    """This class describes some Radius-Vector.
    attr: coords - coords of Vector."""
    def __init__(self, *args):
        self.coords = list(args)

    def __getitem__(self, idx):
        if isinstance(idx, int):
            return self.coords[idx]
        elif isinstance(idx, slice):
            return tuple(self.coords[idx])

    def __setitem__(self, idx, value):
        self.coords[idx] = value