def print_products(*args):
    res = [i for i in args if type(i) == str and i.isalpha()]
    if res:
        for n, item in enumerate(res, 1):
            print(f'{n}) {item}')
    else:
        print('Нет продуктов')
