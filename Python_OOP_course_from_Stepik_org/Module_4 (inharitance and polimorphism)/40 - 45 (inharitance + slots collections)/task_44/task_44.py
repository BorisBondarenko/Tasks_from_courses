class Function:
    """This class describes the interface to work with any possible function.
    By using inheritance and abstract-method _get_function
    (that accepts function from 'outside' by self redefinition),
    we could use the instances of this class to make the arithmetic operation with Function-objects."""

    def __init__(self):
        self._amplitude = 1.0  # amplitude of func
        self._bias = 0.0  # shifting function on axle OY.

    def __call__(self, x, *args, **kwargs):
        return self._amplitude * self._get_function(x) + self._bias

    def _get_function(self, x):
        raise NotImplementedError('метод _get_function должен быть переопределен в дочернем классе')

    def __add__(self, other):
        if type(other) not in (int, float):
            raise TypeError('смещение должно быть числом')

        obj = self.__class__(self._k, self._b)
        obj._bias = self._bias + other
        return obj

    def __mul__(self, other):
        if type(other) not in (int, float):
            raise TypeError('смещение должно быть числом')
        obj = self.__class__(self._k, self._b)
        obj._amplitude = self._amplitude * other
        return obj


class Linear(Function):
    """This class here is like example of using Function-objects."""

    def __init__(self, k, b):
        super().__init__()
        if isinstance(k, self.__class__):
            self._k = k._k
            self._b = k._b
        else:
            self._k = k
            self._b = b

    def _get_function(self, x):
        return self._k * x + self._b  # here I wrote some self func