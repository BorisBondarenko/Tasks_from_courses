def print_fio(name, surname, patronymic):
    res = surname.title()[0] + name.title()[0] + patronymic.title()[0]
    print(res)


name, surname, patronymic = input(), input(), input()
print_fio(name, surname, patronymic)
