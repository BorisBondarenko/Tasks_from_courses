phr = input()

rub = (len(phr) * 60) // 100
ost = (len(phr) * 60) % 100
print(f'{rub} р. {ost} коп.')
