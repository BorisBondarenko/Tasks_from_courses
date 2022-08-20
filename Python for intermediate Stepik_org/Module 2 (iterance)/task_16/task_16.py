n_1 = ['бумага', 'ножницы', 'камень']
n_2 = ['камень', 'бумага', 'ящерица']
n_3 = ['Спок', 'ящерица', 'камень']
n_4 = ['ящерица', 'ножницы', 'Спок']
n_5 = ['Спок', 'бумага', 'ножницы']

all = [n_1, n_2, n_3, n_4, n_5]

ans_1 = input()
ans_2 = input()

for i in all:
    if ans_1 in i and ans_2 in i:
        break

res = i.index(ans_1) - i.index(ans_2)
if res == 1 or res == -2:
    print('Тимур')
elif res == 0:
    print('ничья')
else:
    print('Руслан')
