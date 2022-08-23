class StringException(Exception):
    """Базовый-класс исключений"""
    pass


class NegativeLengthString(StringException):
    """Ошибка, если длина отрицательная"""
    pass


class ExceedLengthString(StringException):
    """Ошибка, если длина превышает заданное значение"""
    pass


try:
    raise ExceedLengthString("Длина превышает заданое значение")
except NegativeLengthString:
    print("NegativeLengthString")
except ExceedLengthString:
    print("ExceedLengthString")
except StringException:
    print("StringException")
