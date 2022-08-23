class PrimaryKeyError(Exception):

    def __init__(self, **kwargs):
        if not kwargs:
            self.message = 'Первичный ключ должен быть целым неотрицательным числом'
        else:
            name, value = list(kwargs.keys())[0], list(kwargs.values())[0]
            self.message = f'Значение первичного ключа {name} = {value} недопустимо'

    def __str__(self):
        return self.message

    def __repr__(self):
        return self.message


try:
    raise PrimaryKeyError(id=-10.5)
except PrimaryKeyError as e:
    print(e)