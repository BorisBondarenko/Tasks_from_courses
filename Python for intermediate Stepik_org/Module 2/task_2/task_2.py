# рост
w = float(input())
# вес
h = float(input())

res = w / pow(h, 2)

if 18.5 <= res <= 25:
    print('Оптимальная масса')
elif 18.5 > res:
    print('Недостаточная масса')
elif res > 25:
    print('Избыточная масса')
