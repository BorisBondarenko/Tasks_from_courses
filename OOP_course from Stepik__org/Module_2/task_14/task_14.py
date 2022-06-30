class PhoneBook:

    def __init__(self):
        self.phone_list = []

    def add_phone(self, phone):
        self.phone_list.append(phone)

    def remove_phone(self, indx):
        self.phone_list.pop(indx)

    def get_phone_list(self):
        return self.phone_list


class PhoneNumber:

    def __init__(self, number, fio):

        if self.check_number(number):
            self.number = number
            self.fio = fio

    @classmethod
    def check_number(cls, number):
        number = str(number)
        return len(number) == 11 and number.isdigit()