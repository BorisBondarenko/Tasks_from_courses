vals = {0: 'Дракон',
        1: 'Змея',
        2: 'Лошадь',
        3: 'Овца',
        4: 'Обезьяна',
        5: 'Петух',
        6: 'Собака',
        7: 'Свинья',
        8: 'Крыса',
        9: 'Бык',
        10: 'Тигр',
        11: 'Заяц'}

year = int(input())
print(vals[(year - 2000) % 12] if year >= 2000 else vals[(12 - (2000 - year) % 12)])
