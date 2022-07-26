a, b = input(), input()

colors = ['синий', 'красный', 'желтый']
if a in colors and b in colors:
    if (a == 'красный' or a == 'желтый') and (b == 'желтый' or b == 'красный'):
        print(a if a == b else 'оранжевый')
    elif (a == 'красный' or a == 'синий') and (b == 'синий' or b == 'красный'):
        print(a if a == b else 'фиолетовый')
    elif (a == 'желтый' or a == 'синий') and (b == 'желтый' or b == 'синий'):
        print(a if a == b else 'зеленый')
else:
    print('ошибка цвета')
