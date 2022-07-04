a, b, c = int(input()), int(input()), int(input())

if a > b and a > c:
    if b + c <= a:
        print('NO')
    else:
        print('YES')

elif b > a and b > c:
    if a + c <= b:
        print('NO')
    else:
        print('YES')


elif c > a and c > b:
    if a + b <= c:
        print('NO')
    else:
        print('YES')