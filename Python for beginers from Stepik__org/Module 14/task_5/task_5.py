def get_month(language, number):
    ru_mon = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
              'декабрь', ]
    en_mon = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
              'november', 'december', ]
    if language == 'ru':
        return ru_mon[number - 1]
    elif language == 'en':
        return en_mon[number - 1]


lan = input()
num = int(input())

print(get_month(lan, num))
