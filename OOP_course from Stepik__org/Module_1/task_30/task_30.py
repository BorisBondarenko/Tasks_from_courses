class CardCheck():
    __LEN = 4

    @classmethod
    def check_card_number(cls, number):
        if len(number.split('-')) == cls.__LEN:
            for i in number.split('-'):
                if i.isdigit() and len(i) == cls.__LEN:
                    return True
                else:
                    return False
        else:
            return False

    @staticmethod
    def check_name(name):
        if len(name.split(' ')) == 2:
            for i in name.split(' '):
                if i.isalpha() and i.isupper() and ord(i[0]) <= 122:
                    return True
                else:
                    return False
        else:
            return False

    def __init__(self, name, number):
        self.name = None
        self.number = None

        if self.check_name(name):
            self.name = name

        if self.check_card_number(number):
            self.number = number