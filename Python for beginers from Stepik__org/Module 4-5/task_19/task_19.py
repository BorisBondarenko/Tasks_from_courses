r = (a, b, c) = int(input()), int(input()), int(input())

if len(set(r)) == 1:
    print('Равносторонний')
elif len(set(r)) == 2:
    print('Равнобедренный')
elif len(set(r)) == 3:
    print('Разносторонний')
