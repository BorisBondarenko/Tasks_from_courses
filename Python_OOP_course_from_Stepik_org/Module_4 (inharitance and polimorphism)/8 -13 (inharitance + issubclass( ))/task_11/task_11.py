class Tuple(tuple):
    """This class male some improvements with tuple-basic type.
    By using this class we can add to our tuples another type objects.
    I just redefined __add__ method."""

    def __add__(self, other):
        other = tuple(other)
        return Tuple(super().__add__(other))
