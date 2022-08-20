all = ['бумага', 'ножницы', 'камень']

n1 = input()
n2 = input()
res = all.index(n1) - all.index(n2)
if res in (1, -2):
    print('Тимур')
elif res == 0:
    print('ничья')
else:
    print('Руслан')
