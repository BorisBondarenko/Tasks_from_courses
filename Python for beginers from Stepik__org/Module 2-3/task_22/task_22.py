dig = int(input())

print(f'Цифра в позиции тысяч равна {dig // 1000}')
print(f'Цифра в позиции сотен равна {(dig // 100) % 10}')
print(f'Цифра в позиции десятков равна {(dig // 10) % 10}')
print(f'Цифра в позиции единиц равна {dig % 10}')