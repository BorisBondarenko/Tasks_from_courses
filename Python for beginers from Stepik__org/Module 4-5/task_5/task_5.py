a = int(input())
b = int(input())
c = int(input())

if a < b < c:
    print('YES' if (c - b) == a else 'NO')
else:
    print('YES' if (a - 2*b) == c else 'NO')