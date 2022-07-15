y = int(input())
print('YES' if not y % 400 or not y % 4 and y % 100 else 'NO')