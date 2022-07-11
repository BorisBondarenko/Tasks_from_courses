n = int(input())
z = 30

if n == 2:
    print(28)

elif 1 <= n < 8:
    if not n % 2:
        print(z)
    else:
        print(z + 1)

elif 8 <= n <= 12:
    if n % 2:
        print(z)
    else:
        print(z + 1)
