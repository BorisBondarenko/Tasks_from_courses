x = int(input())

print('YES' if 999 < x < 10000 and (x % 7 == 0 or x % 17 == 0) else 'NO')