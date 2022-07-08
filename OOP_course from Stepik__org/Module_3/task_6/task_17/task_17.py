class RenderDigit:
    """This class describes the instances that convert str-values to int-type value.
    And in this file using as decoder"""

    def __call__(self, value, *args, **kwargs):
        try:
            return int(value)
        except:
            return None


class InputValues:
    """This is the main class in the file.
    The role of it is to make the join of two function.
    1 - input (to get the string of number) to be decorated by InputValues.
    2 - Function-decoder. In this case it is RenderDigit-instance"""

    def __init__(self, render):
        self.render = render

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            return list(map(self.render, func(*args, **kwargs).split(' ')))

        return wrapper


decoder = RenderDigit()
input_dg = InputValues(decoder)(input)
res = input_dg()
print(res)
