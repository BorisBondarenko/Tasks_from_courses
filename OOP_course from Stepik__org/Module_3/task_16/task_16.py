class InputDigits:
    """"Это класс описывает объекты, что принимают на вход строку из целых числе.
    Результатом работы этих обьектов является список целых чисел, что был принят в строке"""

    def __init__(self, funk):
        self.funk = funk

    def __call__(self, *args, **kwargs):
        def wrapper():
            return list(map(int, self.funk().split(' ')))

        return wrapper()


@InputDigits
def input_dg():
    """Простая функция для ввода целых чисел"""

    string = input()
    return string
