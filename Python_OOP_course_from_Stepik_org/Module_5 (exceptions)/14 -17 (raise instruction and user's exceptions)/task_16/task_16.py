class DateError(Exception):
    pass


class DateString:
    def __init__(self, date_string):
        self.day, self.month, self.year = map(int, date_string.split('.'))

    def __setattr__(self, key, value):
        if key == 'day' and value not in range(1, 31 + 1):
            raise DateError("Неверный формат даты")
        elif key == 'month' and value not in range(1, 12 + 1):
            raise DateError("Неверный формат даты")
        elif key == 'year' and value not in range(1, 3000 + 1):
            raise DateError("Неверный формат даты")
        self.__dict__[key] = value

    def __str__(self):
        return f'{self.day:02}.{self.month:02}.{self.year:04}'


date_string = input()
try:
    date = DateString(date_string)
except DateError as e:
    print(e)
else:
    print(date)
