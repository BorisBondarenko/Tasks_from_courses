phr = input().lower().split(' ')
counter = 0
for i in ('a', 'an', 'the'):
    counter += phr.count(i)
print(f'Общее количество артиклей: {counter}')
