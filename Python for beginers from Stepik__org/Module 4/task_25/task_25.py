n = int(input())
if n == 0:
    print('зеленый')
elif 1 <= n <= 10 or 19 <= n <= 28:
   print('черный' if n % 2 == 0 else 'красный')
elif 11 <= n <= 18 or 29 <= n <= 36:
    print('красный' if n % 2 == 0 else 'черный')
else:
    print('ошибка ввода')