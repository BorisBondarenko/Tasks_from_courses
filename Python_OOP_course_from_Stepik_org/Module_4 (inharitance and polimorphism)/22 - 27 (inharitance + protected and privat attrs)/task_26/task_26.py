def class_log(lst):
    """This decorator should work as logger for each method inside Vector class.
    Every call of method should append name of method inside some external list (vector_log)."""

    def log_methods(cls):
        """Here I apply my decarator-func (meth_decor) for each method in class."""

        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, meth_decor(v))
        return cls

    def meth_decor(func):
        """This is tha main decorator's func.
        Nothing strange or difficult, I just perform appending in list name of func
        without any interfering to method func."""

        def meth_args(*args, **kwargs):
            lst.append(func.__name__)
            return func(*args, **kwargs)

        return meth_args

    return log_methods


vector_log = []


@class_log(vector_log)
class Vector:
    """This class describes some Vector.
    This class should be decorated by class_log."""

    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value
